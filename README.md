# Enterprise Mainframe Batch Operations & GOC Intelligence Framework

An enterprise-grade, production-ready framework designed for 24x7 Global Operations Centres (GOC). This repository automates mainframe batch monitoring, JCL abend triage, Control-MOPC dependency validation, and major incident escalation workflows for core banking operations.

## Architectural Modules
1. JCL Automation Suite Production-tested JCL scripts for core banking interest calculations, statement generation, and DB2 table reorganizations.
2. GOC Event & Incident Engine Python-based monitoring daemon parsing log outputs, classifying abend codes (e.g., S0C4, S322), and triggering automated technical bridges.
3. Scheduler Integration Control-M and OPC workflow validation tools preventing circular dependencies and resource deadlocks.
4. CICD Pipeline Automated syntax checking and validation of JCL and batch configurations via GitHub Actions.