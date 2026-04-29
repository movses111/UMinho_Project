# UMinho_Project
Research Project: "Design and Implementation of the Network Monitoring and Anomaly Detection System for Small-Scale Environments"


## Network Monitoring System for Small Environments

# Project Description

This is a student research project aimed at building a Python-based tool to monitor network devices. The goal is to create a simple system that checks if devices (like servers or routers) are online and alerts the user if something is wrong.

## What this project will do:

- Device Tracking: Keep a list of devices in a json file instead of hardcoding them.
- Status Checks: Use "Ping" to see if a device is active.
- Anomaly Detection: If a device responds too slowly (high latency), the system will mark it as a "problem" even if it is still online.
- Logging: Save all events into a logs.txt file with the exact date and time.

## Technology Stack

- Python: Main programming language.
- JSON: For storing device information.
- Linux: Development environment.
- Git: Version control.

## Project Plan (Roadmap)
- Phase 1: Setup the project structure and learn how to read device lists from a - JSON file. (Current)
- Phase 2: Write the Python script to ping multiple devices automatically.
- Phase 3: Add logic to detect "slow" responses (Simple Anomaly Detection).
- Phase 4: Create a final report and basic notification system
