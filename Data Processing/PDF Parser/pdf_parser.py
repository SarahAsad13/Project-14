import os
from pdfminer.high_level import extract_text

def parse_resume(pdf_file):
    text = extract_text(pdf_file)
    return text

def count_pdfs(directory):
    total_pdfs = 0
    for root, dirs, files in os.walk(directory):
        total_pdfs += sum(1 for filename in files if filename.endswith('.pdf'))
    return total_pdfs

def process_resumes_in_directory(directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    total_pdfs = count_pdfs(directory)
    processed_count = 0
    
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(root, filename)
                parsed_text = parse_resume(pdf_path)
                
                if parsed_text:
                    output_path = os.path.join(output_directory, f"{os.path.splitext(filename)[0]}.txt")
                    with open(output_path, 'w') as f:
                        f.write(parsed_text)
                
                processed_count += 1
                print(f"{processed_count} of {total_pdfs} parsed")
                
def main():
    resumes_directory = 'PDF Parser/Resume data'
    output_directory = 'PDF Parser/Parsed Resumes'
    # Check if the directory exists
    if not os.path.exists(resumes_directory):
        print(f"Directory does not exist: {resumes_directory}")
        return
    
    # Process all resumes in the directory and its subdirectories
    process_resumes_in_directory(resumes_directory, output_directory)

if __name__ == "__main__":
    main()
