# Hiring Assistant Project

This project is designed to assist in the recruitment process by leveraging natural language processing (NLP) techniques to parse resumes, extract relevant information, and store it in a Neo4j graph database for efficient candidate matching.

## Project Structure

The project is structured into several modules:

1. **Data Processing**:
   - **PDF_Parser**: Parses PDF resumes to extract text and relevant data.
   - **NER**: Performs Named Entity Recognition (NER) to identify entities like skills, experience, and education.

2. **Streamlit**: Contains the Streamlit web application for interacting with the Neo4j database and searching for candidates.

3. **Neo4j**: Manages the connection to the Neo4j database and executes queries to fetch candidate data based on search criteria.

4. **Docker**: Docker configuration files for containerizing the application.

## Setup and Installation

### Prerequisites

- Python 3.11.7
- Neo4j Desktop installed and running, accessible at `bolt://localhost:7687`

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SarahAsad13/Project-14
   cd hiring-assistant
