Set-Location $PSScriptRoot
Set-Location ..

$certDir = "certs"

if (!(Test-Path $certDir)) {
    New-Item -ItemType Directory -Path $certDir | Out-Null
}

Write-Host ""
Write-Host "Generating Root CA..."

openssl genrsa -out certs/ca.key 4096

# FIX: proper CA extensions added
@"
basicConstraints=CA:TRUE
keyUsage=keyCertSign,cRLSign
subjectKeyIdentifier=hash
"@ | Set-Content certs/ca.ext

openssl req `
    -x509 `
    -new `
    -nodes `
    -key certs/ca.key `
    -sha256 `
    -days 3650 `
    -out certs/ca.crt `
    -subj "/C=IN/ST=Maharashtra/L=Mumbai/O=TLS Simulation/CN=TLS Demo Root CA" `
    -extfile certs/ca.ext

Write-Host ""
Write-Host "Generating Server Private Key..."

openssl genrsa -out certs/server.key 2048

Write-Host ""
Write-Host "Generating Server CSR..."

openssl req `
    -new `
    -key certs/server.key `
    -out certs/server.csr `
    -subj "/C=IN/ST=Maharashtra/L=Mumbai/O=TLS Simulation/CN=localhost"

@"
subjectAltName=DNS:server,DNS:localhost,IP:127.0.0.1
extendedKeyUsage=serverAuth
keyUsage=digitalSignature,keyEncipherment
"@ | Set-Content certs/server.ext

Write-Host ""
Write-Host "Signing Server Certificate..."

openssl x509 `
    -req `
    -in certs/server.csr `
    -CA certs/ca.crt `
    -CAkey certs/ca.key `
    -CAcreateserial `
    -out certs/server.crt `
    -days 365 `
    -sha256 `
    -extfile certs/server.ext

Write-Host ""
Write-Host "Certificates generated successfully!"