# TCP Client-Server Protocol Simulation using Docker

## Overview

This project is a hands-on networking lab built to understand how network protocols work from the ground up.

The current implementation focuses on:

- TCP socket programming
- Docker container networking
- Client-server communication
- Designing a simple application-layer protocol

The goal is to build toward a complete understanding of HTTPS and TLS by implementing each networking concept in small phases instead of relying on existing frameworks.

---

## Current Phase

### Phase 1 — TCP Communication

Implemented:

- TCP client
- TCP server
- Docker networking
- Socket communication
- Multiple client connections

---

### Phase 2 — Custom Application Protocol

Implemented protocol commands:

| Command | Description |
|----------|-------------|
| `HELLO <name>` | Introduce the client |
| `MSG <message>` | Send a message |
| `PING` | Check server availability |
| `EXIT` | Close the connection |

Example:

```
HELLO Shubham
```

Response:

```
WELCOME Shubham
```

---

## Project Structure

```
.
├── docker-compose.yaml
├── client
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── server
    ├── app.py
    ├── Dockerfile
    └── requirements.txt
```

---

## Running the Project

Build the images:

```bash
docker compose build
```

Start the server:

```bash
docker compose up server
```

Run the client:

```bash
docker compose run --rm client
```

---

## Learning Roadmap

- ✅ Phase 1 – TCP communication
- ✅ Phase 2 – Custom protocol
- ⏳ Phase 3 – Handshake simulation
- ⏳ Phase 4 – Reliability concepts
- ⏳ Phase 5 – Manual encryption
- ⏳ Phase 6 – TLS implementation
- ⏳ Phase 7 – Mutual TLS (mTLS)
- ⏳ Phase 8 – HTTPS simulation

---

## Technologies Used

- Python 3
- Docker
- Docker Compose
- TCP Sockets

---

## Purpose

This repository is intended as a learning project to understand networking and security protocols by implementing them step by step rather than treating them as black boxes.