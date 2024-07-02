import os
import spacy

# Load the language model
nlp = spacy.load("en_core_web_sm")

# Function to extract entities using spaCy NER
def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def count_text_files(directory):
    return sum(1 for filename in os.listdir(directory) if filename.endswith('.txt'))

def process_text_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    total_files = count_text_files(input_directory)
    processed_count = 0

    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            input_path = os.path.join(input_directory, filename)

            # Open and read the file
            with open(input_path, 'r', encoding='utf-8') as f:
                text = f.read()

            # Extract entities using spaCy NER
            entities = extract_entities(text)

            # Write entities to a new file in the output directory
            output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}_ner.txt")
            with open(output_path, 'w') as f:
                for ent, label in entities:
                    f.write(f"{ent}: {label}\n")

            processed_count += 1
            print(f"{processed_count} of {total_files} processed")

def main():
    parsed_resumes_directory = 'PDF Parser/Parsed Resumes'
    ner_output_directory = 'NER/NER Output'
    # Check if the parsed resumes directory exists
    if not os.path.exists(parsed_resumes_directory):
        print(f"Directory does not exist: {parsed_resumes_directory}")
        return
    
    # Process all text files in the parsed resumes directory
    process_text_files(parsed_resumes_directory, ner_output_directory)

if __name__ == "__main__":
    main()