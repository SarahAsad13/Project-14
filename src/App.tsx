import React, { useState } from 'react';
import './App.css'; // Import your CSS file for styling

function App() {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);
  const [processingStatus, setProcessingStatus] = useState<string>('');

  // Handle file upload
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setSelectedFile(file);
    }
  };

  // Handle file upload button click
  const handleUpload = async () => {
    if (selectedFile) {
      // Logic to handle file upload, e.g., send file to backend API
      console.log('Uploading file:', selectedFile.name);

      // Simulate processing status
      setProcessingStatus('Processing in progress...');

      // Placeholder for actual API call to process resume
      try {
        const response = await fetch('http://localhost:8001/upload', {
          method: 'POST',
          body: selectedFile,
          // Headers if required
        });
        // Handle response as needed
        console.log('File upload response:', response);
        setProcessingStatus('Processing completed.');
      } catch (error) {
        console.error('Error uploading file:', error);
        setProcessingStatus('Processing failed.');
      }
    } else {
      alert('Please select a file before uploading.');
    }
  };

  // Handle resume processing (NER and Neo4j)
  const handleProcess = async () => {
    // Placeholder for actual NER and Neo4j processing
    console.log('Processing resume...');
    try {
      const response = await fetch('http://localhost:8001/process', {
        method: 'POST',
        // Body if needed
      });
      // Handle response as needed
      console.log('Resume processing response:', response);
    } catch (error) {
      console.error('Error processing resume:', error);
    }
  };

  // Handle downloading results from Neo4j
  const handleDownload = async () => {
    // Placeholder for downloading results from Neo4j
    console.log('Downloading results...');
    try {
      const response = await fetch('http://localhost:8001/download', {
        method: 'GET',
        // Headers if required
      });
      // Handle response as needed
      console.log('Download results response:', response);
    } catch (error) {
      console.error('Error downloading results:', error);
    }
  };

  return (
    <div className="container">
      <div className="box">
        <h1 className="title">Hiring Assistant</h1>
        <div className="form-container">
          <div className="upload-section">
            <input type="file" onChange={handleFileChange} />
            <button className="btn-blue" onClick={handleUpload}>Process Resume</button>
            <p>Processing status: {processingStatus}</p> {/* Display processing status */}
          </div>
          {/* Download section remains unchanged */}
          <div className="download-section">
            <button className="btn-blue" onClick={handleDownload}>Download Results</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
