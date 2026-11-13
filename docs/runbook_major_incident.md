# 24x7 Global Operations Centre (GOC) Major Incident Runbook

## 1. Scope & Objective
This runbook dictates the protocol for handling high-priority batch failures, system outages, and infrastructure degradations across core banking mainframe environments.

## 2. Incident Lifecycle
* **Detection (T+0 mins):** Alerts received via Splunk dashboards, Control-M/OPC alarms, or automated system hooks.
* **Triage & Classification (T+5 mins):** 
  * Classify incident severity (Sev 1 to Sev 3).
  * Run automated abend diagnostics (`abend_analyzer.py`).
* **Technical Bridge Activation (T+10 mins):** 
  * For Sev 1 incidents, open an emergency bridge line.
  * Invite Major Incident Manager, Lead Mainframe Engineer, and DBA on-call.
* **Resolution & Rerun Execution:** 
  * Apply necessary JCL modifications or dataset allocations.
  * Execute controlled job reruns ensuring upstream/downstream dependency integrity.
* **Post-Incident Review (PIR):** Complete root-cause analysis documentation within 24 hours of resolution.