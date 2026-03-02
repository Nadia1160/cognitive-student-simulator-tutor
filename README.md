## 🐳 Docker Support

This project includes Docker configuration for easy setup and deployment across different environments.

### Prerequisites
- [Docker Desktop](https://docs.docker.com/get-docker/) (Windows/Mac) or Docker Engine (Linux)
- [Docker Compose](https://docs.docker.com/compose/install/) (included with Docker Desktop)
- At least 4GB RAM allocated to Docker (recommended)

### Quick Start with Docker

#### Option 1: Using PowerShell Script (Windows)
```powershell
# Make sure you're in the project directory
cd D:\Nadia\Nadia\Python\Python Projects\cognitive-student-simulator-tutor

# Run the Docker launcher script
.\run_docker.ps1

# You'll see a menu with options:
# 1. Build Docker image
# 2. Run Jupyter notebook server
# 3. Open shell in container
# 4. Run tests
# 5. Stop all containers
# 6. Clean up Docker resources
# 7. Exit