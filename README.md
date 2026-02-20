# Secure Load Balancer with IDS

A Python-based simulation of a secure load balancer integrated with an Intrusion Detection System (IDS) to protect against flood attacks and port scans. The system includes a web dashboard for monitoring logs and simulating client requests.

## Features

- **Load Balancer**: Distributes incoming requests across multiple backend servers using round-robin scheduling.
- **Intrusion Detection System (IDS)**: Monitors network traffic using Scapy to detect and block flood attacks and port scans by adding IPs to a blacklist.
- **Blacklist Management**: Shared utilities for checking and updating a blacklist of blocked IPs.
- **Logging**: Centralized logging of system events, accessible via a web API.
- **Web Dashboard**: Flask-based frontend with buttons to simulate normal requests, flood attacks, and port scans, plus live log display.
- **Client Simulators**: Scripts to mimic normal traffic, DDoS floods, and port scans.

## Prerequisites

- Python 3.7+
- Required packages: `flask`, `scapy` (install via `pip install flask scapy`)

## Installation

1. Clone or download the project.
2. Navigate to the project root directory.
3. Install dependencies:

## Usage

1. **Start the Servers**: Run multiple backend servers on different ports (e.g., 9001, 9002, 9003).


2. **Start the Load Balancer**: Run the load balancer on port 8000.


3. **Start the IDS**: Run the IDS to monitor traffic (requires admin privileges for packet sniffing).


4. **Start the Frontend Dashboard**: Run the Flask app on port 5000.


5. **Access the Dashboard**: Open a browser to `http://127.0.0.1:5000` to view logs and simulate requests.

- Use the buttons to run client simulators: normal requests, floods, or port scans.
- Logs update in real-time via the `/api/logs` endpoint.

## Architecture

- **Frontend** ([frontend/app.py](frontend/app.py)): Flask app serving the dashboard and triggering client scripts.
- **Load Balancer** ([load_balancer/load_balancer.py](load_balancer/load_balancer.py)): Handles requests, checks blacklist, detects floods, forwards to servers.
- **IDS** ([ids/ids.py](ids/ids.py)): Sniffs packets to detect anomalies and update blacklist.
- **Servers** ([server/server.py](server/server.py)): Simple socket servers responding to requests.
- **Clients** ([client/](client/)): Scripts simulating different types of traffic.
- **Shared Utilities** ([shared/](shared/)): Logger ([shared/logger.py](shared/logger.py)) and blacklist ([shared/blacklist.py](shared/blacklist.py)) management.

## Configuration

- Adjust flood/port scan thresholds in [load_balancer/load_balancer.py](load_balancer/load_balancer.py) and [ids/ids.py](ids/ids.py).
- Blacklist is stored in [logs/blacklist.txt](logs/blacklist.txt).

## License

This project is for educational purposes only. Use responsibly.
