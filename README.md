# EIS-2026: Industrial Sovereign Autonomy Standard

![System Demo](https://github.com/user-attachments/assets/a5e85f07-6f4f-494e-940e-d618deea9f76)

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Standard: FDO](https://img.shields.io/badge/Standard-FDO%202.0-orange.svg)](https://fairdo.org)
[![Status: Sovereign](https://img.shields.io/badge/Status-Sovereign-green.svg)]()

> **The eFDO Framework**: A reference implementation for Kinetic FAIR Digital Objects (K-FDO) with self-sovereign identity, decentralized anchoring, and state-based commercial licensing.

---

## 🏗 System Architecture

The EIS-2026 standard defines a closed-loop ecosystem for industrial assets. It ensures technical sovereignty through four distinct layers:

### 1. Identity Layer (`did_generator.py`)
Implementation of **W3C Decentralized Identifiers (DID)**. It generates immutable `did:efdo:uuid` via `Ed25519` cryptographic keys, granting assets their own digital birthright.

### 2. Kinetic Layer (`robot_adapter.py`)
The "Physical-Digital" bridge. It injects real-time industrial telemetry (Torque, Temperature) and maintains a **Physical Circuit Breaker** to trigger halts during anomalies.

### 3. Storage Layer (`ipfs_anchor.py`)
State snapshots are hashed and pinned to the **IPFS** network. This creates a content-addressable, tamper-proof audit trail for the asset's entire lifecycle.

### 4. Commercial Layer (`license_vault.py`)
Dynamic enforcement of **GPL-3.0**. The system autonomously revokes the API `ACCESS_TOKEN` if the asset's health index falls below safety thresholds.

---

## 📐 Mathematical Model

The value and sovereign state of an eFDO asset are dynamically calculated using the following formula:

$$V_{\mathrm{kinetic}} = V_{\mathrm{base}} \times (1 - \mathrm{Fatigue\_Index}) \times \alpha$$

**Where:**
* $\mathrm{Fatigue\_Index} = f(\mathrm{Torque}, \mathrm{Temp})$
* **Alpha ($\alpha$):** Sovereign Coefficient (1.0 for valid license, 0.0 for revoked/halted).

---

## 🚀 Quick Start (STABLE DEPLOYMENT)

Follow these steps to initialize the sovereign node.

### Step 1: Launch the Sovereign Monitor
Execute the real-time telemetry and dashboard service:

```bash
python3 live_monitor.py

### Step 2: Execute the Sovereign Publish Cycle
./publish.sh
(Workflow: Evolve -> Inject Data -> Anchor IPFS -> Update License)

---

## 📜 Sovereign Licensing & Compliance

Protected under GPL-3.0 License.

- Status GREEN: Asset health is normal. ACCESS_TOKEN is valid.
- Status RED: Asset is fatigued (Index > 95%). License is REVOKED.

---
Author: Zhang Bin (FDO Architect)
Contact: joy7759@gmail.com
Lab: Sovereign Node 01 (Mac-Mini-ZB)
