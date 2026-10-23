# AICTE Integrated Institution Complaint Monitoring & Tracking Dashboard
**Smart India Hackathon 2026 (SIH 2026) Official Solution**

> **A centralized, AI-assisted compliance and grievance tracking platform for AICTE officials to monitor, coordinate, and expedite institution complaints across the Regulation Bureau (RB), Public Grievance Redressal Cell (PGRC), Approval Bureau (AB), and Regional Offices.**

---

## 🎯 Executive Summary & Objective

In higher and technical education governance, technical institutions often face multiple concurrent inquiries from different AICTE bureaus without mutual coordination. For example:
- A faculty complaint regarding **unpaid 7th Pay Commission salaries** may be lodged with the **Public Grievance Redressal Cell (PGRC)**.
- Concurrently, an inspection alleging **ghost faculty or violation of mandatory faculty cadres** may be initiated by the **Regulation Bureau (RB)**.

Without integration, this leads to **duplicated hearings, conflicting regulatory orders, administrative delay, and institutional evasion**.

This dashboard provides a unified, cross-bureau intelligence hub with **AI-assisted overlap detection**, enabling AICTE officers to spot concurrent proceedings, cross-reference findings, share compliance orders, and maintain a permanent chronological audit trail.

---

## 🚀 Key Modules & Capabilities

### 1. AI-Assisted Cross-Bureau Overlap Detection Engine (Flagship Innovation)
- **Deterministic AICTE Permanent ID Match:** Instant 100% correlation on institutional permanent identifiers (e.g., `1-3324567891`).
- **Cross-Bureau Clash Rule:** Detects when Regulation Bureau (RB) and Public Grievance Redressal Cell (PGRC) are simultaneously probing the same institution.
- **Categorical Correlation & Description Similarity:** Uses N-gram tokenization and Jaccard keyword overlap to identify related regulatory allegations.
- **Human-in-the-Loop Safeguard:** Alerts officers with **"Potential Overlapping Cases – Coordination Required"**. Never auto-merges or auto-closes files; enables officers to record joint coordination remarks and link files.

### 2. Multi-Role Government Enterprise Access
- **Regulation Bureau (RB) Officer:** Focuses on regulatory non-compliance, show-cause notices, and committee hearings.
- **PGRC Officer:** Focuses on student/faculty grievance redressal and ombudsman hearings.
- **System Administrator:** Full platform oversight, configuration, and audit logs.
- **Regional Officer (WRO / NRO / SRO):** Regional jurisdiction filtering and physical inspection tracking.
- **Senior Management (Advisor / Member Secretary):** Executive disposal metrics, escalation approvals, and council reports.

### 3. Comprehensive Complaint Lifecycle & Immutable Timeline
- Full metadata tracking: Case ID, AICTE Permanent ID, Institution details, Category, Priority, Bureau, Officer, SLA Due Date, Overdue tracking.
- Permanent chronological action history recording every notice, order, evidence submission, and status change.
- Statuses: `Pending`, `Under Process`, `Disposed`, `Transferred`, `Escalated`.

### 4. Institution Registry & Dossier Profiles
- Master directory of AICTE approved institutions.
- Direct drill-down into complete historical complaints, linked cross-bureau cases, and active regulatory sanctions.

### 5. Interactive Analytics & Live Data Visualizations
- Bureau-wise complaint distribution.
- Monthly complaints received vs disposed (disposal velocity).
- Pending case ageing analysis (`<15 days`, `15-30 days`, `30-60 days`, `>60 days` overdue).
- Regional jurisdiction spread (Western, Northern, Southern, North-West, Eastern).
- 1-click **Official CSV Report Export**.

---

## ⚡ Quick Start: How to Run the Application

The application is fully self-contained and pre-bundled for instant demonstration:

### Option A: Immediate Browser Launch (Zero-install Python Server)
```powershell
# Open terminal in the project directory
cd "d:\sih hackthon"

# Launch local server
python -m http.server 5173

# Open your browser and navigate to:
http://127.0.0.1:5173/
```
*(Alternatively, you can double-click `index.html` to open it directly in any browser.)*

### Option B: Node.js / Vite Development Workflow (When Node.js is installed)
```bash
npm install
npm run dev
```

---

## 🏆 Smart India Hackathon 2026 Live Demo Walkthrough

When presenting to SIH 2026 judges, follow this 3-minute demo script:

1. **Official Sign-In:**
   - On the login screen, point out the official AICTE header and SIH 2026 badge.
   - Click the **"Regulation Bureau (RB)"** instant role selector button.
   - Click **"Authenticate & Enter Secure Portal"**.

2. **Central Dashboard Overview:**
   - Highlight the 7 summary metric cards (Total Complaints, Pending, Under Process, Disposed, Transferred, Overdue, and Overlap Detected).
   - Show the 5 interactive charts: Bureau distribution, Monthly trends, Case ageing, Regional breakdown, and Complaint status pipeline.

3. **Demonstrate Cross-Bureau Overlap (The SIH 2026 Scenario):**
   - Click the prominent amber button: **"🔥 SIH 2026 Live Demo: RB ⟷ PGRC Overlap"**.
   - Show the detected overlap between:
     - **Case 1 (`AICTE/RB/2026/0104`):** Regulation Bureau investigating Apex Institute of Technology for 7th Pay Commission non-compliance & ghost faculty.
     - **Case 2 (`AICTE/PGRC/2026/0218`):** PGRC processing 14 faculty petitions regarding 6 months unpaid salaries and original certificate retention.
   - Show the **92% AI Similarity Score** and match justifications.
   - Click **"Link Related Cases & Coordinate"**.
   - Enter joint inspection remarks and click **"Confirm Joint Linking & Notify Officers"**.
   - Show that both case files now display synchronized cross-reference badges and mutual audit log updates!

4. **Complaint Registration & Live Scan:**
   - Click **"Register New Complaint"**.
   - Register a grievance against any institution and show how the system immediately runs real-time duplicate checks.

5. **Official Audit Export:**
   - Click **"Export CSV"** to generate a downloadable spreadsheet of all case records.

---

## 🛡️ Security & Privacy Notice
All institutional records, faculty names, and complaint narratives provided in this prototype are realistic synthetic demo fixtures created for the Smart India Hackathon 2026. No confidential government or private personal data is used.

Developed for **Smart India Hackathon 2026**.
