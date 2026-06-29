# TCP Client-Server Simulation (Docker)

## Overview
This project simulates a basic TCP client-server architecture using Python sockets inside Docker containers.

It demonstrates:
- TCP socket communication
- Client-server message exchange
- JSON-based protocol over raw TCP
- Docker networking between containers

## Architecture

Client (Python) <----TCP----> Server (Python)

Both run in separate Docker containers connected via Docker bridge network.

## Run Instructions

```bash
docker compose up --build
```