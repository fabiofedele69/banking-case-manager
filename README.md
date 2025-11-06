# Banking Case Manager — Helm + Postgres (Minikube)

This guide deploys the app via Helm and uses the included Kubernetes manifests for PostgreSQL.

**Preconditions:**
- Minikube installed and running
- kubectl installed
- Helm installed
- Docker (or use Minikube's docker daemon)

**Default DB values used in files (replace POSTGRES_PASSWORD before prod):**
- DB_HOST: pg-bank-postgresql
- DB_PORT: 5432
- DB_NAME: postgres
- DB_USER: postgres
- DB_PASSWORD: password123  (placeholder)

## Step-by-step

### 1) Start Minikube (if not running)
```bash
minikube start
