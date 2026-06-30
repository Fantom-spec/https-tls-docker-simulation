# ==============================
# HTTPS TLS Docker Simulation
# Folder Setup
# ==============================

$folders = @(
    "client",
    "server",
    "certs",
    "scripts"
)

foreach ($folder in $folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "[+] Created $folder"
    }
}

$files = @(
    "README.md",

    "client/app.py",
    "client/requirements.txt",

    "server/app.py",
    "server/requirements.txt",

    "scripts/generate_certs.ps1"
)

foreach ($file in $files) {
    if (!(Test-Path $file)) {
        New-Item -ItemType File -Path $file | Out-Null
        Write-Host "[+] Created $file"
    }
}

Write-Host ""
Write-Host "Project structure created successfully!"