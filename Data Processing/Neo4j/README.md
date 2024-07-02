# Neo4j Uploader

This folder contains the script for uploading extracted entities to Neo4j.

## Setup
1. Download and install Neo4j 

   Download Neo4j Desktop
   Install and set up a local database. 
   Navigate to Neo4j directory
2. Install dependencies:
    
    pip install -r requirements.txt

3. Ensure NER output files are in the `NER/NER_Output` directory.

4. Open Neo4j Desktop and ensure the local database is running: neo4j start
   Verify that the Neo4j server is accessible at localhost:7687.

5. Execute the Neo4j script in VS Code to insert data into the database:

    python Neo4j.py
    
6. Data will be uploaded to the Neo4j database.

