# Credit Card Fraud Detection App

This is a Streamlit web application for detecting fraudulent credit card transactions using machine learning. The application allows users to upload a dataset of credit card transactions and processes it to identify potential fraud.

## Features

- Upload credit card transactions dataset (Excel format)
- Preprocesses the data for analysis
- Applies machine learning models to detect anomalies

## Dataset

You can download the sample dataset for credit card transactions from the following link:

[Credit Card Transactions Dataset](<[dataset-url>](https://docs.google.com/spreadsheets/d/1uuLzSFuG7AgCCmscqIn3AKaPiZIxA_E6/edit?usp=sharing&ouid=102888038537900014131&rtpof=true&sd=true))

Replace `<dataset-url>` with the actual URL where the dataset is hosted.

## Installation

To run this application, you need to have Python installed along with the required libraries.

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
