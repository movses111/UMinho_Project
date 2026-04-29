# UMinho_Project
Research Project: "Design and Implementation of the Network Monitoring and Anomaly Detection System for Small-Scale Environments"

## Project Overview

This research explores the design and implementation of a lightweight, automated network monitoring system specifically optimized for small-scale IT infrastructures. The goal is to move beyond simple connectivity checks and implement an intelligent Anomaly Detection Engine that identifies network performance degradation before service failure occurs.

## Research Objectives

- Infrastructure Observability: Developing a robust data collection engine to monitor device availability and network latency.
- Baseline Analysis: Establishing performance baselines to distinguish between normal operation and network anomalies.
- Automated Diagnostics: Implementing automated verification of critical network services (ICMP, TCP/UDP).
- Data-Driven Configuration: Using structured data formats (JSON/YAML) to ensure scalable and modular configuration management.

## Technology Stack

- Language: Python (for automation and logic)
- Data Handling: JSON (for dynamic device inventory)
- Operating System: Linux (VirtualBox environment)
- Version Control: Git


## System Architecture (Current Progress)

- Configuration Layer: JSON-based asset management for dynamic device tracking.
- Modular Design: Separated monitoring logic and logging engines to ensure high code maintainability.
- Logging Engine: Standardized event logging with ISO 8601 timestamps for forensic analysis.

## Implementation Roadmap

- Initial Project Structure & Configuration Management.
- Phase 2: Multi-protocol Data Acquisition (ICMP & Port Scanning).
- Phase 3: Statistical Anomaly Detection Logic (Latency thresholds).
- Phase 4: Alerting & Automated Reporting System.