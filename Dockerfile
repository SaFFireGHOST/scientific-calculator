FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python3", "main.py"]

# Use Python 3.11 slim image as base
FROM python:3.11-slim



# Set working directory inside container
WORKDIR /app
COPY . /app
# Create a non-root user for security
RUN groupadd -r calcuser && useradd -r -g calcuser calcuser


# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Create logs directory and set permissions
RUN mkdir -p /app/logs && chown -R calcuser:calcuser /app

# Switch to non-root user
USER calcuser

# Expose port (if needed for future web interface)
EXPOSE 8080

# Set environment variables
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1


# Default command to run the calculator
CMD ["python3", "main.py"]
