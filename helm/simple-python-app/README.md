# Simple Python App Helm Chart

This Helm chart deploys a simple Flask application to Kubernetes.

## Prerequisites

- Kubernetes 1.19+
- Helm 3.2.0+
- Docker image built and available in your registry

## Installing the Chart

To install the chart with the release name `my-simple-app`:

```bash
helm install my-simple-app ./helm/simple-python-app
```

The command deploys the Flask application on the Kubernetes cluster in the default configuration. The [Parameters](#parameters) section lists the parameters that can be configured during installation.

> **Tip**: List all releases using `helm list`

## Uninstalling the Chart

To uninstall/delete the `my-simple-app` deployment:

```bash
helm uninstall my-simple-app
```

The command removes all the Kubernetes components associated with the chart and deletes the release.

## Parameters

### Global parameters

| Name                      | Description                                     | Value |
| ------------------------- | ----------------------------------------------- | ----- |
| `nameOverride`            | String to partially override common.names.name | `""`  |
| `fullnameOverride`        | String to fully override common.names.fullname | `""`  |

### Image parameters

| Name                | Description                                                                             | Value              |
| ------------------- | --------------------------------------------------------------------------------------- | ------------------ |
| `image.repository`  | Flask application image repository                                                      | `simple-python-app` |
| `image.tag`         | Flask application image tag (immutable tags are recommended)                           | `""`               |
| `image.pullPolicy`  | Flask application image pull policy                                                     | `IfNotPresent`     |

### Deployment parameters

| Name                                    | Description                                                                               | Value   |
| --------------------------------------- | ----------------------------------------------------------------------------------------- | ------- |
| `replicaCount`                          | Number of Flask application replicas to deploy                                           | `2`     |
| `podAnnotations`                        | Annotations for Flask application pods                                                    | `{}`    |
| `podSecurityContext.enabled`            | Enabled Flask application pods' Security Context                                          | `true`  |
| `podSecurityContext.fsGroup`            | Set Flask application pod's Security Context fsGroup                                     | `2000`  |
| `containerSecurityContext.enabled`      | Enabled Flask application containers' Security Context                                    | `true`  |
| `containerSecurityContext.runAsUser`    | Set Flask application containers' Security Context runAsUser                              | `1000`  |
| `containerSecurityContext.runAsNonRoot` | Set Flask application containers' Security Context runAsNonRoot                           | `true`  |
| `containerSecurityContext.readOnlyRootFilesystem` | Set Flask application containers' Security Context readOnlyRootFilesystem            | `false` |

### Service parameters

| Name                        | Description                                                                                                                      | Value       |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `service.type`              | Flask application service type                                                                                                   | `ClusterIP` |
| `service.port`              | Flask application service HTTP port                                                                                              | `80`        |
| `service.targetPort`        | Flask application service HTTP target port                                                                                       | `5000`      |

### Ingress parameters

| Name                       | Description                                                                                                                      | Value                    |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| `ingress.enabled`          | Enable ingress record generation for Flask application                                                                           | `false`                  |
| `ingress.className`        | IngressClass that will be used to implement the Ingress (Kubernetes 1.18+)                                                     | `""`                     |
| `ingress.annotations`      | Additional annotations for the Ingress resource                                                                                  | `{}`                     |
| `ingress.hosts[0].host`    | Default host for the ingress record                                                                                              | `simple-python-app.local` |
| `ingress.hosts[0].paths`   | Default paths for the ingress record                                                                                             | `["/"]`                  |
| `ingress.tls`              | TLS configuration for additional hostname(s) to be covered with this ingress record                                             | `[]`                     |

### Resource parameters

| Name                       | Description                                                                                                                      | Value   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `resources.limits`         | The resources limits for the Flask application containers                                                                        | `{}`    |
| `resources.requests`       | The requested resources for the Flask application containers                                                                     | `{}`    |

### Autoscaling parameters

| Name                                       | Description                                                                                                                      | Value   |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `autoscaling.enabled`                      | Enable Horizontal POD autoscaling for Flask application                                                                          | `false` |
| `autoscaling.minReplicas`                  | Minimum number of Flask application replicas                                                                                     | `2`     |
| `autoscaling.maxReplicas`                  | Maximum number of Flask application replicas                                                                                     | `10`    |
| `autoscaling.targetCPUUtilizationPercentage` | Target CPU utilization percentage                                                                                              | `80`    |

### Other parameters

| Name                       | Description                                                                                                                      | Value   |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `nodeSelector`             | Node labels for Flask application pods assignment                                                                                | `{}`    |
| `tolerations`              | Tolerations for Flask application pods assignment                                                                                | `[]`    |
| `affinity`                 | Affinity for Flask application pods assignment                                                                                   | `{}`    |

### Environment variables

| Name          | Description                    | Value           |
| ------------- | ------------------------------ | --------------- |
| `env.FLASK_ENV` | Flask environment             | `production`    |
| `env.FLASK_APP` | Flask application entry point | `app.py`        |

### Health check parameters

| Name                                    | Description                                                                                                                      | Value   |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `healthCheck.enabled`                   | Enable readiness probe                                                                                                           | `true`  |
| `healthCheck.path`                      | Path for the readiness probe                                                                                                     | `/healthz` |
| `healthCheck.initialDelaySeconds`       | Initial delay for readiness probe                                                                                                | `30`    |
| `healthCheck.periodSeconds`             | Period for readiness probe                                                                                                       | `10`    |
| `healthCheck.timeoutSeconds`            | Timeout for readiness probe                                                                                                      | `5`     |
| `healthCheck.failureThreshold`          | Failure threshold for readiness probe                                                                                            | `3`     |
| `livenessProbe.enabled`                 | Enable liveness probe                                                                                                            | `true`  |
| `livenessProbe.path`                    | Path for the liveness probe                                                                                                      | `/healthz` |
| `livenessProbe.initialDelaySeconds`     | Initial delay for liveness probe                                                                                                 | `30`    |
| `livenessProbe.periodSeconds`           | Period for liveness probe                                                                                                        | `10`    |
| `livenessProbe.timeoutSeconds`          | Timeout for liveness probe                                                                                                       | `5`     |
| `livenessProbe.failureThreshold`        | Failure threshold for liveness probe                                                                                             | `3`     |

## Configuration and installation details

### Deploy chart

1. Create namespace (optional):
   ```bash
   kubectl create namespace simple-python
   ```

2. Build and push Docker image:
   ```bash
   docker build -t your-registry/simple-python-app:latest .
   docker push your-registry/simple-python-app:latest
   ```

3. Update `values.yaml` with your image repository:
   ```yaml
   image:
     repository: your-registry/simple-python-app
     tag: latest
   ```

4. Install the chart:
   ```bash
   helm install my-simple-app ./helm/simple-python-app --namespace simple-python
   ```

### Enable ingress

To enable ingress, set `ingress.enabled=true` and configure your ingress controller:

```bash
helm install my-simple-app ./helm/simple-python-app \
  --set ingress.enabled=true \
  --set ingress.hosts[0].host=your-domain.com
```

### Enable autoscaling

To enable horizontal pod autoscaling:

```bash
helm install my-simple-app ./helm/simple-python-app \
  --set autoscaling.enabled=true \
  --set autoscaling.minReplicas=2 \
  --set autoscaling.maxReplicas=10
```

## Examples

### Production deployment

```bash
helm install my-simple-app ./helm/simple-python-app \
  --set replicaCount=3 \
  --set resources.limits.cpu=1000m \
  --set resources.limits.memory=1Gi \
  --set resources.requests.cpu=500m \
  --set resources.requests.memory=512Mi \
  --set ingress.enabled=true \
  --set ingress.hosts[0].host=api.mycompany.com \
  --set autoscaling.enabled=true
```

### Development deployment

```bash
helm install my-simple-app ./helm/simple-python-app \
  --set replicaCount=1 \
  --set resources.limits.cpu=250m \
  --set resources.limits.memory=256Mi \
  --set env.FLASK_ENV=development
```
