<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# Digital Decay

## Basic Details

### Team Name: BRAIN WAVE

### Team Members
- Member 1: Nourin M S - Jyothi engineering college thrissur
- Member 2: Parvathy Binoy-Jyothi engineering college thrissur

### Hosted Project Link
https://tink-her-hack-parvathybinoy0fficial.streamlit.app/

### Project Description
Digital Decay is a Streamlit web app that scans local storage to find duplicate and blurry images, helping users clean digital clutter.
By reducing unnecessary data, it estimates potential CO₂ savings, promoting sustainable digital habits.

### The Problem statement
In today’s digital world, people store thousands of images, screenshots, and media files on their devices and cloud storage. Many of these files are duplicates or blurry/low-quality, which take up unnecessary storage space.
This not only clutters devices but also increases energy consumption in data centers, contributing to a larger digital carbon footprint. Currently, there is no easy way for users to automatically identify and remove such digital waste, making digital cleanup tedious and inefficient.

### The Solution
Digital Decay provides an automated and user-friendly web application to help users clean their digital storage.
It scans folders to detect duplicate images using hash-based comparison.
It identifies blurry or low-quality images using OpenCV-based image analysis.
It presents a dashboard showing storage usage, duplicate/blurry counts, and estimated digital carbon footprint.
Users can preview and delete unwanted files selectively or in bulk, freeing storage and reducing energy consumption.
In short:
A one-stop solution to clean digital clutter, save storage, and reduce digital carbon emissions.



## Technical Details

### Technologies/Components Used

**For Software:**
- Languages used: Python
- Frameworks used: streamlit
- Libraries used: Opencv,PIL,matplotlib
- Tools used: VS code,Github

## Features

List the key features of your project:
- Feature 1: scans folder to detect duplicate images using hash based comparison
- Feature 2: identifies blury or low quality images using open cv based image analysis
- Feature 3:Display storae usage statistics and duplicate/blury image counts through a simple dashboard
- Feature 4: allows users to preview and delete unwanted images to free up storage space


## Implementation

### For Software:

#### Installation
# Clone the repository
git clone https://github.com/ParvathybinoyOfficial/tink-her-hack-temp.git

# Navigate to the project directory
cd tink-her-hack-temp

# Install required dependencies
pip install -r requirements.txt

#### Run
# Run the Streamlit application
streamlit run app.py



## Project Documentation

### For Software:

#### Screenshots (Add at least 3)

Screenshot1-https://github.com/Parvathybinoy0fficial/tink-her-hack-temp/blob/main/Screenshot%202026-02-14%20075509.png

login 
user id

Screenshot2-<https://github.com/Parvathybinoy0fficial/tink-her-hack-temp/blob/main/Screenshot%202026-02-14%20075536.png

file pathway
                
Screenshot3- https://github.com/Parvathybinoy0fficial/tink-her-hack-temp/blob/main/Screenshot%202026-02-14%20084002.png

#### Diagrams

**System Architecture:**
User Interface (UI)
Streamlit frontend: login page, folder input, dashboard metrics, image views, buttons for deletion.
Session Management
Streamlit session_state: Tracks login status and selected files across interactions.
File System Scanner
os and pathlib: Reads folder contents, gets image file paths, file sizes, and metadata.
Duplicate Detection Module
hashlib: Computes MD5 hash of each image to identify duplicates.
Blurry Image Detection Module
OpenCV (cv2): Detects blur using Laplacian variance.
Storage & CO₂ Estimation Module
Calculates total image storage in GB and estimates CO₂ saved (storage_gb * 0.5 kg CO₂/GB).
Visualization Module
matplotlib + Streamlit: Shows bar charts (originals, duplicates, blurry), dashboard metrics.
Action Module
Allows user to delete single or multiple files (duplicates/blurry) using os.remove().

**Application Workflow:**


Login
User enters username & password
If correct → Access main app
If wrong → Show error
Folder Selection / Input
User selects a folder path to scan
File Scanning
App reads all images in folder (.jpg, .png, .jpeg)
Stores metadata (file path, size, hash)
Processing / Analysis
Duplicate Detection: Compare hashes of files
Blurry Image Detection: Use OpenCV Laplacian method
Storage & CO₂ Estimation: Calculate total size and potential carbon savings




## Project Demo

### Video
https://youtu.be/LbPSeuBt9os?si=dUrXCYjOzMXCH2ps
video demonstrates the working of how the digital decay website works



## Team Contributions

- Nourin M S – Project lead, backend development using Python, image processing with OpenCV, duplicate detection logic, and overall application integration.
 Testing, debugging, documentation (README)




-Parvathy binoy – Frontend development using Streamlit, UI design, dashboard creation, and user interaction handling.
 Testing, debugging, documentation (README), and project presentation/demo preparation.
