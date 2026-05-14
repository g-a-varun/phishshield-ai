\# API Design: PhishShield AI



\## Purpose of This Document



This document defines the backend API structure for PhishShield AI.



The API will allow external applications, dashboards, and future email integrations to send email data to the system and receive phishing risk analysis.



The backend will be built using FastAPI.



\---



\## API Development Strategy



The first working project will use Streamlit directly.



FastAPI will be added after the core ML pipeline is working.



The reason is simple:



```text

First make the model work.

Then expose it through an API.

Then connect dashboard and database.

