
---

# Sly's AI - ATS Resume Checker

Sly's AI is a powerful web application designed to evaluate resumes against job descriptions using the advanced capabilities of Google Gemini. It helps job seekers optimize their resumes by identifying missing keywords and providing a tailored profile summary based on the job description. This tool simulates the behavior of an Applicant Tracking System (ATS) with an emphasis on fields like Artificial Intelligence, Machine Learning, Software Engineering, Data Science, Data Analytics, and Cyber Security.

---

## Features
- **Resume Evaluation**: Analyze resumes by comparing them to specific job descriptions.
- **Match Percentage**: Get a quantified matching score indicating how well the resume aligns with the job description.
- **Missing Keywords**: Identify key terms missing from the resume that are relevant to the job.
- **Profile Summary**: Generate a professional profile summary tailored to the job description.

---

## Tech Stack
- **Frontend**: Streamlit  
- **Backend**: Google Gemini API (via `google.generativeai`)  
- **Languages**: Python  
- **Libraries Used**:
  - `dotenv` for managing environment variables
  - `streamlit` for creating the user interface
  - `PyPDF2` for reading and extracting text from PDF resumes
  - `Pillow` for image handling (optional for future features)
  - `google.generativeai` for leveraging Google Gemini's advanced generative capabilities

---

## How It Works
1. **Input**:
   - Upload your resume (PDF format).
   - Enter the job description in the provided text area.

2. **Processing**:
   - Extract text from the uploaded resume using `PyPDF2`.
   - Send the resume and job description to Google Gemini's generative AI model using a predefined prompt.
   - Generate insights, including the match percentage, missing keywords, and a profile summary.

3. **Output**:
   - Display the AI-generated evaluation as a structured JSON-like string with the following fields:
     - `JD Match`: The percentage match between the resume and job description.
     - `MissingKeywords`: A list of important terms missing from the resume.
     - `Profile Summary`: A tailored professional summary based on the job description.

---

## Setup and Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ATS-Resume-Checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ATS-Resume-Checker
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   - Create a `.env` file in the project root directory.
   - Add your Google API key:
     ```plaintext
     GOOGLE_API_KEY=your_google_api_key
     ```

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## Usage
1. Launch the app and navigate to the URL displayed in your terminal.
2. Enter the job description in the provided text area.
3. Upload your resume in PDF format.
4. Click the **Submit** button to view the analysis results.

---

## Future Enhancements
- Add support for other file formats (e.g., DOCX).
- Include advanced analytics like keyword density and ATS-specific formatting suggestions.
- Provide downloadable reports for resume improvement.
- Enable multilingual support for resumes and job descriptions.

---

## Contributing
Contributions are welcome! If you'd like to improve the project, feel free to fork the repository and submit a pull request.  

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- [Google Gemini API](https://developers.google.com/) for powering the generative AI features.
- [Streamlit](https://streamlit.io/) for the seamless UI framework.
- Open-source contributors for making development tools and libraries available.

---
