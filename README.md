# EIS-2026: Industrial Sovereign Autonomy Standard

![System Demo]](https://github.com/user-attachments/assets/a5e85f07-6f4f-494e-940e-d618deea9f76)


[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Standard: FDO](https://img.shields.io/badge/Standard-FDO%202.0-orange.svg)](https://fairdo.org)
[![Status: Sovereign](https://img.shields.io/badge/Status-Sovereign-green.svg)]()

> **The eFDO Framework**: A reference implementation for Kinetic FAIR Digital Objects (K-FDO) with self-sovereign identity, decentralized anchoring, and state-based commercial licensing.

---

## 🏗 System Architecture (架构全景)

The EIS-2026 standard defines a closed-loop ecosystem for industrial assets:

1.  **Identity Layer (`did_generator.py`)**
    - **Standard**: W3C DID (Decentralized Identifiers).
    - **Mechanism**: Generates immutable `did:efdo:uuid` based on `Ed25519` cryptographic keys.

2.  **Kinetic Layer (`robot_adapter.py`)**
    - **Telemetry**: Real-time injection of Torque (Nm) and Temperature (°C).
    - **Safety**: Implements a "Physical Circuit Breaker" that triggers `CRITICAL_HALT`.

3.  **Storage Layer (`ipfs_anchor.py`)**
    - **Anchoring**: Periodic state snapshots are hashed (CID) and pinned to the **IPFS** network.

4.  **Commercial Layer (`license_vault.py`)**
    - **Dynamic Licensing**: Automatically manages **GPL-3.0** compliance.
    - **Rule**: If `Fatigue_Index > 95%`, the API Token is revoked.

---

## 📐 Mathematical Model (核心算法)

The value of an eFDO asset is dynamically calculated based on its kinetic health:

$$V_{kinetic} = V_{base} \times (1 - \text{Fatigue\_Index}) \times \alpha$$

Where:
- $\text{Fatigue\_Index} = f(\text{Torque}, \text{Temp})$
- $\alpha$: Sovereign Coefficient (1.0 for valid license, 0.0 for revoked).

---

## 🚀 Quick Start (一键部署)

Initialize the sovereign node and start the lifecycle:

### 1. Start the Sovereign Monitor
```bash
python3 live_monitor.py
# Access: http://localhost:8000/dashboard.html
