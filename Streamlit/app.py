# Streamlit/app.py

import streamlit as st
from py2neo import Graph

# Set up the connection to Neo4j
uri = "bolt://localhost:7687"  
username = "neo4j"  # Update with your Neo4j username
password = "hello123"  # Update with your Neo4j password

# Initialize the graph object
graph = Graph(uri, auth=(username, password))

# Streamlit app title
st.title("Hiring Assistant")

# Streamlit app description
st.write("""
This Streamlit app allows users to search and display results from the Neo4j graph database.
""")
with st.form(key='search_form'):
    st.write("Enter your search criteria:")
    skills = st.text_input("Skills (comma-separated):", "Python, SQL, machine learning algorithms")
    experience_years = st.number_input("Minimum years of experience:", min_value=0, max_value=50, value=3)
    industry = st.text_input("Industry:", "fintech")
    location = st.text_input("Location:", "New York City")
    education = st.text_input("Education:", "Bachelor’s degree in Computer Science or related field")
    certification = st.text_input("Certifications:", "Certified Scrum Master (CSM)")
    teamwork = st.selectbox("Teamwork:", ["", "strong", "average", "weak"])
    adaptability = st.selectbox("Adaptability:", ["", "high", "medium", "low"])
    submit_button = st.form_submit_button(label='Search')

if submit_button:
    # Process the input
    skills_list = [skill.strip() for skill in skills.split(',')]    

    # Create the Cypher query
    query = f"""
    MATCH (c:Candidate)-[:HAS_ENTITY]->(e:Entity)
    WHERE all(skill IN {skills_list} WHERE skill IN e.name)
      AND c.experience >= {experience_years}
      AND c.industry = '{industry}'
      AND c.location = '{location}'
      AND c.education CONTAINS '{education}'
      AND '{certification}' IN c.certifications
    """

    if teamwork:
        query += f" AND c.teamwork = '{teamwork}'"
    if adaptability:
        query += f" AND c.adaptability = '{adaptability}'"
    
    query += " RETURN c.name AS CandidateName, c.location AS Location, c.experience AS ExperienceYears"
    
    try:
        # Run the query
        candidates = graph.run(query).data()
        
        # Display the results
        if candidates:
            st.write("### Matching Candidates:")
            for candidate in candidates:
                st.write(f"**Name:** {candidate['CandidateName']}")
                st.write(f"**Location:** {candidate['Location']}")
                st.write(f"**Years of Experience:** {candidate['ExperienceYears']}")
                st.write("---")
        else:
            st.write("No candidates found matching the criteria.")
    except Exception as e:
        st.error(f"Error running query: {e}")
       