# HTTPS over TLS Simulation with Python & Wireshark

## Overview

This project is a hands-on networking lab built to demonstrate how HTTPS works on top of TLS. Instead of relying on a web framework, the project uses Python's standard networking libraries to create a minimal HTTPS client and server, making it easier to observe the underlying protocol behavior.

The primary goal is to understand the complete lifecycle of a secure connection by analyzing packet captures in Wireshark.

---

## Features

* HTTPS server using TLS
* HTTPS client making secure requests
* Self-signed Certificate Authority (CA)
* Server certificate generation with OpenSSL
* End-to-end encrypted communication
* Packet capture analysis using Wireshark

---

## Project Structure

```text
.
├── certs/
│   ├── ca.crt
│   ├── server.crt
│   └── ...
├── scripts/
│   ├── generate_certs.ps1
│   └── reset_project.ps1
├── screenshots/
│   ├── tcp_handshake.png
│   ├── client_hello.png
│   ├── server_hello.png
│   ├── certificate.png
│   └── application_data.png
├── captures/
│   └── https_tls_handshake.pcapng
├── client.py
├── server.py
└── README.md
```

---

## Technologies

* Python 3
* OpenSSL
* HTTPS
* TLS
* Wireshark

---

## Running the Project

Generate the certificates:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\generate_certs.ps1
```

Start the server:

```powershell
python server.py
```

In another terminal, start the client:

```powershell
python client.py
```

---

## Capturing Traffic

1. Open Wireshark.
2. Start capturing on the appropriate loopback interface.
3. Apply the filter:

```text
tcp.port == 8443
```

Observe the complete HTTPS connection, including:

* TCP Three-Way Handshake
* TLS Client Hello
* TLS Server Hello
* Certificate Exchange
* Encrypted Application Data

---

## Sample Capture

The repository includes:

* A sample Wireshark capture (`.pcapng`)
* Screenshots of important protocol stages

These allow the TLS handshake to be explored without running the project.

---

## Learning Objectives

This project demonstrates:

* TCP connection establishment
* TLS handshake sequence
* Certificate-based authentication
* Cipher suite negotiation
* Encrypted HTTPS communication
* Packet-level protocol analysis with Wireshark

---

## Future Enhancements

* Mutual TLS (mTLS)
* TLS 1.2 vs TLS 1.3 comparison
* Certificate validation improvements
* TLS session resumption
* HTTP/2 over TLS
* TLS key logging for Wireshark decryption

---

## Purpose

The purpose of this repository is educational. It provides a minimal HTTPS implementation that can be inspected with Wireshark to understand how secure web communication is established, authenticated, and encrypted at the protocol level.
