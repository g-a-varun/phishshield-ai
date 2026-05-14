\# Project Scope: PhishShield AI



\## Project Title



PhishShield AI: AI-Driven Multilingual Phishing Detection System for Indian Enterprises



\## Problem Statement



Indian enterprises face increasingly sophisticated phishing attacks, including AI-generated, personalized, multilingual, and Tamil-English code-mixed phishing emails. Traditional rule-based filters often fail to detect malicious intent, behavioral anomalies, and contextual manipulation.



\## Project Goal



Build an AI-powered system that analyzes enterprise emails and detects phishing attempts using multilingual NLP, intent detection, behavioral anomaly analysis, and explainable risk scoring.



\## Target Users



1\. Enterprise employees  

2\. IT security teams  

3\. Security administrators  

4\. Small and medium business owners  



\## MVP Input



The first version of the system will accept:



\- email subject

\- email body

\- sender email address

\- receiver email address

\- timestamp, optional

\- URLs inside the email



For the MVP, users will manually paste the email details into the dashboard.



\## MVP Output



The system will return:



\- phishing or legitimate classification

\- phishing probability

\- risk score from 0 to 100

\- risk level: Low, Medium, High, or Critical

\- detected intent

\- language type: English, Tamil, or Tamil-English code-mixed

\- suspicious indicators

\- explanation for the prediction



\## Core Modules



\### 1. Email Parsing Module

Extracts useful parts from the email, including subject, body, sender, receiver, URLs, and metadata.



\### 2. Preprocessing Module

Cleans email text, removes unnecessary HTML, normalizes spacing, extracts URLs, and prepares text for ML models.



\### 3. Multilingual NLP Classifier

Classifies emails as phishing or legitimate using baseline ML models first, then transformer-based multilingual models.



\### 4. Intent Detection Module

Identifies the likely malicious intent behind the email, such as credential theft, invoice fraud, fake IT support, payment redirection, or urgency manipulation.



\### 5. Behavioral Anomaly Module

Detects unusual communication patterns, such as unknown sender, suspicious domain, unusual request, or abnormal urgency.



\### 6. Risk Scoring Engine

Combines phishing probability, intent risk, and behavioral anomaly score into a final risk score.



\### 7. Dashboard

Displays the email analysis result, risk score, explanation, and scan history.



\## MVP Features



\- Manual email input

\- URL extraction

\- Text preprocessing

\- Baseline phishing classifier

\- Risk score generation

\- Intent detection version 1

\- Simple behavioral anomaly scoring

\- Streamlit dashboard

\- Result history storage later



\## Not Included in MVP



\- Gmail/Outlook real-time integration

\- Full enterprise email gateway

\- Browser extension

\- Automatic production retraining

\- Real-time organization-wide monitoring

\- Advanced LLM agent workflow



These may be added in later versions.



\## Success Metrics



The MVP will be considered successful if it can:



\- classify phishing vs legitimate emails using a baseline ML model

\- generate a meaningful risk score

\- identify at least basic malicious intent categories

\- show explanations for suspicious indicators

\- run through a simple dashboard

\- produce measurable evaluation metrics such as accuracy, precision, recall, F1-score, and false positive rate



\## Initial Tech Stack



\- Python

\- Pandas

\- NumPy

\- Scikit-learn

\- Matplotlib

\- Seaborn

\- FastAPI

\- Streamlit

\- PostgreSQL later

\- Hugging Face Transformers later

\- Docker later



\## Current Phase



Project setup and scope definition.

