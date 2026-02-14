<p align="center">
  <img src="./img.png" alt="Project Banner" width="100%">
</p>

# [Project Name] 🎯

## Basic Details

### Team Name: [Name]

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

![Screenshot1]https://github.com/Parvathybinoy0fficial/tink-her-hack-temp/blob/main/Screenshot%202026-02-14%20075509.png

login 
user id

![Screenshot2]<https://github.com/Parvathybinoy0fficial/tink-her-hack-temp/blob/main/Screenshot%202026-02-14%20075536.png

file pathway
                

![Screenshot3]https://github.com/Parvathybinoy0fficial/tink-her-hack-temp/blob/main/Screenshot%202026-02-14%20084002.png

#### Diagrams

**System Architecture:**

![Architecture Diagram](docs/architecture.png)
*Explain your system architecture - components, data flow, tech stack interaction*

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




---

## Additional Documentation

### For Web Projects with Backend:

#### API Documentation

**Base URL:** **Base URL:** `http://localhost:8501`

##### Endpoints

**GET /api/endpoint**
- **Description:** scan a folder for duplicate and blury images
- **Parameters:**
  - `param1` (string): folder_path (string): Path of the folder to scan
  - `param2` (integer): [Description]
- **Response:**
{
  "status": "success",
  "data": {
    "duplicates": 5,
    "blurry": 3,
    "storage_gb": 0.8,
    "co2_kg": 0.4
  }
}

**POST /api/endpoint**
- **Description:** delete selected duplicate or blury files
- **Request Body:**
{
  "files": ["file1.jpg", "file2.png"]
}
- **Response:**
{
  "status": "success",
  "message": "Selected files deleted successfully"
}

[Add more endpoints as needed...]



## Project Demo

### Video
https://github.com/Parvathybinoy0fficial/tink-her-hack-temp/blob/main/Screen%20Recording%202025-12-14%20135226.mp4
video demonstrates the working of how the digital daey website works

### Additional Demos
[Add any extra demo materials/links - Live site, APK download, online demo, etc.]

---

## AI Tools Used (Optional - For Transparency Bonus)

If you used AI tools during development, document them here for transparency:

**Tool Used:** [e.g., GitHub Copilot, v0.dev, Cursor, ChatGPT, Claude]

**Purpose:** [What you used it for]
- Example: "Generated boilerplate React components"
- Example: "Debugging assistance for async functions"
- Example: "Code review and optimization suggestions"

**Key Prompts Used:**
- "Create a REST API endpoint for user authentication"
- "Debug this async function that's causing race conditions"
- "Optimize this database query for better performance"

**Percentage of AI-generated code:** [Approximately X%]

**Human Contributions:**
- Architecture design and planning
- Custom business logic implementation
- Integration and testing
- UI/UX design decisions

*Note: Proper documentation of AI usage demonstrates transparency and earns bonus points in evaluation!*

---

## Team Contributions

- [Name 1]: [Specific contributions - e.g., Frontend development, API integration, etc.]
- [Name 2]: [Specific contributions - e.g., Backend development, Database design, etc.]
- [Name 3]: [Specific contributions - e.g., UI/UX design, Testing, Documentation, etc.]

---

## License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

**Common License Options:**
- MIT License (Permissive, widely used)
- Apache 2.0 (Permissive with patent grant)
- GPL v3 (Copyleft, requires derivative works to be open source)

---

Made with ❤️ at TinkerHub
