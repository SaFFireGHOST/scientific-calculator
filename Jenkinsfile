pipeline {
  agent any
  environment {
    DOCKER_REPO = "saffireghost/sci-calculator"
  }
  stages {
    stage('Checkout') {
      steps { checkout scm }
    }
    stage('Test') {
      steps {
        sh 'python3 -m venv venv || true'
        sh '. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt && PYTHONPATH=. pytest -q'
      }
    }
    stage('Build Docker') {
      steps {
        script {
          IMAGE_TAG = "${DOCKER_REPO}:${env.BUILD_NUMBER}"
          sh "docker build -t ${IMAGE_TAG} ."
          sh "docker tag ${IMAGE_TAG} ${DOCKER_REPO}:latest"
        }
      }
    }
    stage('Push Docker') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
          sh "docker push ${DOCKER_REPO}:${env.BUILD_NUMBER}"
          sh "docker push ${DOCKER_REPO}:latest"
        }
      }
    }
    stage('Deploy via Ansible') {
      steps {
        sh "ansible-playbook -i ansible/inventory ansible/deploy.yml --extra-vars \"image=${DOCKER_REPO}:${env.BUILD_NUMBER}\""
      }
    }
  }
  post {
    success {
      emailext(
        subject: "Jenkins Build Success: ✅ ${env.JOB_NAME} #${env.BUILD_NUMBER}",
        body: "Good news!\nThe build for job '${env.JOB_NAME}' (build #${env.BUILD_NUMBER}) was successful.\n\nCheck console output: ${env.BUILD_URL}",
        to: "mupparapukoushik@gmail.com"
      )
    }
    failure {
      emailext(
        subject: "Jenkins Build Failed: ❌ ${env.JOB_NAME} #${env.BUILD_NUMBER}",
        body: "The build for job '${env.JOB_NAME}' (build #${env.BUILD_NUMBER}) has FAILED.\n\nCheck logs: ${env.BUILD_URL}",
        to: "mupparapukoushik@gmail.com"
      )
    }
  }
}
