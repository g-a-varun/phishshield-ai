\# Dataset Plan: PhishShield AI



\## Dataset Goal



The project needs a dataset that can train and evaluate an AI-driven phishing detection system for Indian enterprises.



The dataset should support:



\- phishing vs legitimate classification

\- multilingual phishing detection

\- Tamil-English code-mixed phishing detection

\- malicious intent detection

\- URL and metadata-based risk scoring



\## Required Data Types



\### 1. English Phishing Emails



Used for training the initial phishing classifier.



Examples:



\- credential theft emails

\- fake bank alerts

\- fake IT support messages

\- invoice fraud emails

\- account suspension emails

\- malicious link emails



\### 2. English Legitimate Emails



Used as the non-phishing class.



Examples:



\- normal workplace communication

\- meeting updates

\- HR announcements

\- project updates

\- invoice confirmations

\- support responses



\### 3. Tamil Phishing Emails



Used to support regional language phishing detection.



Examples:



\- fake bank warnings in Tamil

\- account verification scams in Tamil

\- fake government/office communication in Tamil



\### 4. Tamil-English Code-Mixed Emails



Used to handle realistic Indian workplace communication.



Examples:



\- English + Tamil mixed phishing emails

\- Tamil transliterated using English letters

\- corporate-style messages with regional language phrases



\### 5. URL Data



Used for extracting suspicious URL features.



Examples:



\- shortened URLs

\- IP-based URLs

\- suspicious domains

\- mismatched links

\- login-looking URLs



\### 6. Simulated Enterprise Behavior Data



Used for behavioral anomaly analysis.



Examples:



\- usual sender-receiver pairs

\- usual communication time

\- usual sender domains

\- usual request types

\- normal email frequency



\## Dataset Schema



The main dataset should use this structure:



| Column | Description |

|---|---|

| email\_id | Unique email ID |

| subject | Email subject |

| body | Email body |

| sender | Sender email address |

| receiver | Receiver email address |

| timestamp | Email timestamp |

| urls | Extracted URLs |

| language | English / Tamil / Tamil-English |

| label | 0 = legitimate, 1 = phishing |

| intent\_label | Type of phishing intent |

| source | Dataset source |

| is\_synthetic | Whether the sample was synthetically created |



\## Intent Labels



The first version will use these intent categories:



| Intent Label | Meaning |

|---|---|

| credential\_theft | Trying to steal login credentials |

| invoice\_fraud | Fake invoice or billing fraud |

| payment\_redirection | Asking to send money to a different account |

| urgency\_manipulation | Creating pressure or fear |

| fake\_hr | Fake HR/job/employee communication |

| fake\_bank | Fake banking or financial alert |

| fake\_it\_support | Fake IT/admin/support request |

| malware\_lure | Tricking user to download/open malicious file |

| benign | No malicious intent |



\## Initial Dataset Target



For the first MVP:



| Data Type | Target Count |

|---|---:|

| English phishing emails | 2,000+ |

| English legitimate emails | 2,000+ |

| Tamil phishing emails | 300+ |

| Tamil-English code-mixed phishing emails | 300+ |

| Tamil/Tamil-English legitimate emails | 300+ |

| Simulated enterprise behavior records | 500+ |



These numbers can increase later.



\## Dataset Sources



Possible public sources:



\- Kaggle phishing email datasets

\- SpamAssassin public corpus

\- Enron email dataset for legitimate emails

\- Nazario phishing corpus

\- PhishTank URL dataset

\- OpenPhish URL feed, if accessible



Tamil and Tamil-English samples may be created using:



\- manual writing

\- careful translation from English phishing patterns

\- synthetic generation followed by manual review

\- workplace-style legitimate samples written manually



\## Data Quality Rules



The dataset must avoid:



\- duplicate emails

\- empty body text

\- unclear labels

\- private personal information

\- real passwords, phone numbers, or sensitive data

\- overfitting patterns such as every phishing email containing the same keywords



\## Train-Test Split Plan



The dataset will be split into:



\- 70% training data

\- 15% validation data

\- 15% test data



The test set must include:



\- English phishing

\- English legitimate

\- Tamil phishing

\- Tamil-English phishing

\- legitimate Tamil/Tamil-English samples



\## Evaluation Metrics



The models will be evaluated using:



\- accuracy

\- precision

\- recall

\- F1-score

\- false positive rate

\- confusion matrix



For phishing detection, precision and recall are more important than raw accuracy.



\## Current Dataset Phase



Dataset planning in progress.

