# Text cleaning utilities for PhishShield AI.
# This module contains helper functions to clean email subject/body text before feature extraction and model training.

import re
from bs4 import BeautifulSoup

def remove_html_tags (text:str) -> str:
    
    if not isinstance (text, str):
        return ""
    
    soup = BeautifulSoup(text, "lxml")
    return soup.get_text(separator=" ")

def replace_urls (text:str) -> str:

    if not isinstance(text, str):
        return ""
    
    url_pattern = r"(https?://\S+|www\.\S+)"
    return re.sub(url_pattern, " URL ", text)

def normalize_whitespace (text: str) -> str:

    if not isinstance(text, str):
        return ""
    
    return re.sub(r"\s+", " ", text).strip()

def clean_email_text (text: str, lowercase: bool = True) -> str:

    if not isinstance(text, str):
        return ""
    
    text = remove_html_tags(text)
    text = replace_urls(text)

    if lowercase:
        text = text.lower()

    text = normalize_whitespace(text)

    return text

def combine_subject_body (subject: str, body: str) -> str:
    
    subject = subject if isinstance(subject, str) else ""
    body = body if isinstance(body, str) else ""

    combined_text = f"{subject} {body}"
    return clean_email_text(combined_text)