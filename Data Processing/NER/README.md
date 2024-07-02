# Named Entity Recognition (NER) Extractor

This folder contains the script for extracting named entities from parsed resumes.

## Setup
Change the directory to NER
1. Install dependencies:

    pip install -r requirements.txt

2. Download spaCy model
    python -m spacy download en_core_web_sm

3. Ensure parsed resumes are in the `PDF Parser/Parsed_Resumes` directory.

4. Run the NER extractor script:
   
    python NER.py
   

5. NER output will be saved in the `NER_Output` directory.
