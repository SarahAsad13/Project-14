from neo4j import GraphDatabase
import os

# Neo4j connection details
uri = "bolt://localhost:7687"  # Adjust this URI based on your Neo4j server location and port
user = "neo4j"
password = "hello123"

# Create a Neo4j driver instance
driver = GraphDatabase.driver(uri, auth=(user, password))

# Function to create nodes and relationships in Neo4j
def create_graph_entities(tx, entities, filename):
    candidate_name = os.path.splitext(filename)[0]
    tx.run("MERGE (c:Candidate {name: $name})", name=candidate_name)
    for entity in entities:
        if len(entity) == 2:
            entity_name, label = entity
            tx.run("MERGE (e:Entity {name: $entity, label: $label})", entity=entity_name, label=label)
            tx.run("""
                MATCH (c:Candidate {name: $candidate_name}), (e:Entity {name: $entity, label: $label})
                MERGE (c)-[:HAS_ENTITY]->(e)
                """, candidate_name=candidate_name, entity=entity_name, label=label)

def process_ner_files(directory):
    with driver.session() as session:
        for filename in os.listdir(directory):
            if filename.endswith('_ner.txt'):
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as f:
                    entities = [line.strip().split(": ") for line in f.readlines() if ": " in line]
                session.execute_write(create_graph_entities, entities, filename)

def main():
    ner_output_directory = 'NER/NER Output'
    
    # Check if the NER output directory exists
    if not os.path.exists(ner_output_directory):
        print(f"Directory does not exist: {ner_output_directory}")
        return
    
    # Process all NER files in the directory
    process_ner_files(ner_output_directory)

if __name__ == "__main__":
    main()