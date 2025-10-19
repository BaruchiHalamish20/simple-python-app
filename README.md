# Simple Python Flask Application

A simple Flask web application that demonstrates basic routing and template rendering functionality.

## Features

- **Endpoint Discovery**: Visit `/oshri` to see all available endpoints
- **Student Page**: Dynamic student page rendering using templates
- **Health Check**: Built-in health check endpoint
- **Docker Support**: Fully containerized with Docker

## Available Endpoints

- `GET /oshri` - Returns JSON with all available endpoints
- `GET /student/<name>` - Renders a student page with the provided name
- `GET /healthz` - Health check endpoint

## Quick Start

### Using Docker (Recommended)

1. Build the Docker image:
   ```bash
   docker build -t simple-python-app .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 simple-python-app
   ```

3. Access the application:
   - Open your browser and go to `http://localhost:5000`
   - Visit `http://localhost:5000/oshri` to see available endpoints
   - Try `http://localhost:5000/student/John` to see a student page

### Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Access the application at `http://localhost:5000`

## Project Structure

```
simple-python/
├── app.py                 # Main Flask application
├── templates/
│   └── student.html      # Student page template
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker configuration
├── .dockerignore        # Docker ignore file
├── helm/
│   └── simple-python-app/    # Helm chart for Kubernetes deployment
│       ├── Chart.yaml       # Chart metadata
│       ├── values.yaml      # Default configuration values
│       ├── templates/       # Kubernetes manifests
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   ├── ingress.yaml
│       │   ├── configmap.yaml
│       │   ├── serviceaccount.yaml
│       │   ├── hpa.yaml
│       │   └── _helpers.tpl
│       └── README.md        # Helm chart documentation
└── README.md           # This file
```

## Dependencies

- Flask: Web framework for Python

## Development

The application runs in debug mode by default when started locally. It's configured to:
- Listen on all interfaces (`0.0.0.0`)
- Use port 5000
- Enable debug mode for development

## Docker

The application is containerized and ready for deployment. The Dockerfile:
- Uses Python 3.11 slim base image
- Installs dependencies from requirements.txt
- Exposes port 5000
- Runs the Flask application

## Kubernetes Deployment with Helm

The application includes a complete Helm chart for deploying to Kubernetes clusters.

### Prerequisites

- Kubernetes cluster (1.19+)
- Helm 3.2.0+
- kubectl configured to access your cluster

### Quick Deploy to Kubernetes

1. **Build and push your Docker image**:
   ```bash
   # Build the image
   docker build -t your-registry/simple-python-app:latest .
   
   # Push to your registry
   docker push your-registry/simple-python-app:latest
   ```

2. **Deploy using Helm**:
   ```bash
   # Create namespace (optional)
   kubectl create namespace simple-python
   
   # Deploy the application
   helm install my-simple-app ./helm/simple-python-app \
     --namespace simple-python \
     --set image.repository=your-registry/simple-python-app \
     --set image.tag=latest
   ```

3. **Access the application**:
   ```bash
   # Port forward to access locally
   kubectl port-forward svc/my-simple-app 8080:80 -n simple-python
   
   # Or expose via LoadBalancer
   kubectl patch svc my-simple-app -n simple-python -p '{"spec":{"type":"LoadBalancer"}}'
   ```

### Production Deployment

For production, use additional configuration:

```bash
helm install my-simple-app ./helm/simple-python-app \
  --namespace simple-python \
  --set image.repository=your-registry/simple-python-app \
  --set replicaCount=3 \
  --set resources.limits.cpu=1000m \
  --set resources.limits.memory=1Gi \
  --set ingress.enabled=true \
  --set ingress.hosts[0].host=api.yourcompany.com \
  --set autoscaling.enabled=true \
  --set autoscaling.minReplicas=2 \
  --set autoscaling.maxReplicas=10
```

### Helm Chart Features

- **Deployment**: Configurable replica count and resource limits
- **Service**: ClusterIP service with configurable ports
- **Ingress**: Optional ingress for external access
- **ConfigMap**: Environment configuration
- **ServiceAccount**: Dedicated service account
- **HPA**: Optional horizontal pod autoscaling
- **Health Checks**: Readiness and liveness probes
- **Security**: Pod security contexts and non-root user

For detailed Helm configuration options, see [helm/simple-python-app/README.md](helm/simple-python-app/README.md).

## Example Usage

1. **List endpoints**:
   ```bash
   curl http://localhost:5000/oshri
   ```

2. **View student page**:
   ```bash
   curl http://localhost:5000/student/Alice
   ```

3. **Health check**:
   ```bash
   curl http://localhost:5000/healthz
   ```
