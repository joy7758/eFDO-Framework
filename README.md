# EIS-2026: Industrial Sovereign Autonomy Standard

![System Demo](https://github.com/user-attachments/assets/a5e85f07-6f4f-494e-940e-d618deea9f76)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Standard: FDO](https://img.shields.io/badge/Standard-FDO%202.0-orange.svg)](https://fairdo.org)
[![Status: Sovereign](https://img.shields.io/badge/Status-Sovereign-green.svg)]()

> **The eFDO Framework**: A reference implementation for Kinetic FAIR Digital Objects (K-FDO) with self-sovereign identity, decentralized anchoring, and state-based commercial licensing.

---

## 🏗 System Architecture (架构全景)

The EIS-2026 standard defines a closed-loop ecosystem for industrial assets:

### Identity Layer (`did_generator.py`)
* **Standard**: W3C DID (Decentralized Identifiers).
* **Mechanism**: Generates immutable `did:efdo:uuid` based on `Ed25519` cryptographic keys.

### Kinetic Layer (`robot_adapter.py`)
* **Telemetry**: Real-time injection of Torque (Nm) and Temperature (°C).
* **Safety**: Implements a "Physical Circuit Breaker" that triggers `CRITICAL_HALT`.

### Storage Layer (`ipfs_anchor.py`)
* **Anchoring**: Periodic state snapshots are hashed (CID) and pinned to the **IPFS** network.

### Commercial Layer (`license_vault.py`)
* **Dynamic Licensing**: Automatically manages **GPL-3.0** compliance.
* **Rule**: If `Fatigue\_Index > 95%`, the API Token is revoked.

---

## 📐 Mathematical Model (核心算法)

The value of an eFDO asset is dynamically calculated based on its kinetic health:

$$V_{\mathrm{kinetic}} = V_{\mathrm{base}} \times (1 - \mathrm{Fatigue\_Index}) \times \alpha$$

Where:
* $\mathrm{Fatigue\_Index} = f(\mathrm{Torque}, \mathrm{Temp})$
* $\alpha$: Sovereign Coefficient (1.0 for valid license, 0.0 for revoked).

---

## 🚀 Quick Start (一键部署)

Initialize the sovereign node and start the lifecycle:

### Step 1: Start the Sovereign Monitor
Launch the real-time telemetry dashboard service:
```bash
python3 live_monitor.py
Dashboard URL: http://localhost:8000/dashboard.html
### Step 2: Execute the Sovereign Publish Cycle
In a new terminal, trigger the industrial data injection pipeline:
```bash
Workflow: Evolve -> Inject Data -> Anchor IPFS -> Update License
./publish.sh
📜 Sovereign Licensing & Compliance
This framework is protected under the GPL-3.0 License.

Commercial Enforcement Protocol:

Status GREEN: Asset health is normal. ACCESS_TOKEN is valid and active.

Status RED: Asset is fatigued (Index > 95%). License is REVOKED automatically, and the system returns ACCESS_DENIED.

Author: Zhang Bin (FDO Architect) Contact: joy7759@gmail.com Lab: Sovereign Node 01 (Mac-Mini-ZB)
