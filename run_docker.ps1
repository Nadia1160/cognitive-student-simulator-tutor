#!/usr/bin/env pwsh

Write-Host "🐳 Cognitive Student Simulator Tutor - Docker Launcher" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan

function Show-Menu {
    Write-Host "
Choose an option:" -ForegroundColor Yellow
    Write-Host "1. Build Docker image"
    Write-Host "2. Run Jupyter notebook server"
    Write-Host "3. Open shell in container"
    Write-Host "4. Run tests"
    Write-Host "5. Stop all containers"
    Write-Host "6. Clean up Docker resources"
    Write-Host "7. Exit"
}

while (True) {
    Show-Menu
     = Read-Host "
Enter your choice (1-7)"
    
    switch () {
        "1" {
            Write-Host "
🔨 Building Docker images..." -ForegroundColor Green
            docker-compose build
        }
        "2" {
            Write-Host "
🚀 Starting Jupyter server..." -ForegroundColor Green
            Write-Host "Access Jupyter at: http://localhost:8888" -ForegroundColor Yellow
            docker-compose up jupyter
        }
        "3" {
            Write-Host "
🐚 Opening shell in dev container..." -ForegroundColor Green
            docker-compose run --rm dev /bin/bash
        }
        "4" {
            Write-Host "
🧪 Running tests..." -ForegroundColor Green
            docker-compose run --rm test
        }
        "5" {
            Write-Host "
🛑 Stopping all containers..." -ForegroundColor Green
            docker-compose down
        }
        "6" {
            Write-Host "
🧹 Cleaning up Docker resources..." -ForegroundColor Green
            docker-compose down -v
            docker system prune -f
        }
        "7" {
            Write-Host "
👋 Goodbye!" -ForegroundColor Cyan
            exit
        }
        default {
            Write-Host "
❌ Invalid choice. Please try again." -ForegroundColor Red
        }
    }
}
