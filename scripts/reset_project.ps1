# ============================================
# Reset Project - Remove Docker Components
# ============================================

Write-Host "Removing Docker-related files..."

# Remove docker-compose
if (Test-Path "docker-compose.yaml") {
    Remove-Item "docker-compose.yaml" -Force
    Write-Host "Removed docker-compose.yaml"
}

if (Test-Path "docker-compose.yml") {
    Remove-Item "docker-compose.yml" -Force
    Write-Host "Removed docker-compose.yml"
}

# Remove Dockerfiles
Get-ChildItem -Path . -Recurse -Filter Dockerfile | ForEach-Object {
    Remove-Item $_.FullName -Force
    Write-Host "Removed $($_.FullName)"
}

# Remove Docker capture folder
if (Test-Path "captures") {
    Remove-Item "captures" -Recurse -Force
    Write-Host "Removed captures folder"
}

# Remove __pycache__
Get-ChildItem -Path . -Directory -Recurse -Filter "__pycache__" | ForEach-Object {
    Remove-Item $_.FullName -Recurse -Force
}

Write-Host ""
Write-Host "Docker-related files removed."
Write-Host "Certificates, scripts, Python files and Git files were preserved."