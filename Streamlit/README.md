# Streamlit App

This folder contains the Streamlit app for the candidate search engine. The app allows users to upload resumes, parse them, extract entities, and search for candidates based on specific criteria.

## Setup

1. Create and actvate a virtual environment and activate it:

    python -m venv venv
    source /venv/bin/activate

2. Install dependencies:

    pip install -r requirements.txt


3. Open Neo4j Desktop and ensure it is running on localhost:7687.

4. Change the username and password in `app.py` (Line 9) to the one given by you when you created the graph.

5. Run the Streamlit app:

    streamlit run app.py 
