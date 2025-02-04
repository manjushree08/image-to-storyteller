# Image to Storyteller 🚀

A powerful AI-driven application that transforms images into engaging stories using Hugging Face models.
The interface is built using three methods AWS SageMaker for inference,Direct inference API and local call for the model.
The backend models used are image to text, llm and text to speech generation.The application generate simple funny immersive story.

<<<<<<< HEAD
  <img src="/uploads/App_Screen.png" alt="Application Screenshot" width="600"/>

## Features 🎯

=======
## Features 🎯
>>>>>>> 26c5b7025d5092c082d1f178bbc75b42de82e756
- 📷 **Image Processing**: Upload an image via an HTML page and let AI analyze it.
- 📝 **Story Generation**: Uses an LLM to craft compelling narratives based on image content.
- 🎙 **Speech Synthesis**: Converts the generated text into speech for an immersive storytelling experience.
- ☁️ **Cloud Deployment**: Scalable inference using AWS SageMaker.

## Tech Stack 🛠
<<<<<<< HEAD

=======
>>>>>>> 26c5b7025d5092c082d1f178bbc75b42de82e756
- **Hugging Face**: For deep learning models and image-to-text conversion.
- **AWS SageMaker**: For cloud-based model inference.
- **Backend LLM App**: Manages prompt engineering and story generation.
- **Speech Generator**: Converts text into lifelike narration.
- **Flask/FastAPI**: Backend API for processing requests.
- **HTML & JavaScript**: Frontend for image upload and user interaction.

## Installation 📦
<<<<<<< HEAD

=======
>>>>>>> 26c5b7025d5092c082d1f178bbc75b42de82e756
1. Clone the repository:
   ```bash
   git clone https://github.com/manjushree08/image-to-storyteller.git
   cd image-to-storyteller
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage 🚀
<<<<<<< HEAD

=======
>>>>>>> 26c5b7025d5092c082d1f178bbc75b42de82e756
1. Run the backend service:
   ```bash
   python app.py
   ```
2. Open `index.html` in a web browser and upload an image.
3. The backend will process the image, generate a story, and return the narrated version.

## AWS SageMaker Deployment ☁️
<<<<<<< HEAD

To deploy the model on AWS SageMaker:

=======
To deploy the model on AWS SageMaker:
>>>>>>> 26c5b7025d5092c082d1f178bbc75b42de82e756
1. Train and save the model:
   ```python
   deployment.py
   ```

## Contributing 🤝
<<<<<<< HEAD

Contributions are welcome! To contribute:

=======
Contributions are welcome! To contribute:
>>>>>>> 26c5b7025d5092c082d1f178bbc75b42de82e756
1. Fork the repo.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to GitHub (`git push origin feature-branch`).
5. Submit a pull request.

## License 📜
<<<<<<< HEAD

This project is licensed for **Personal Use Only**. Redistribution or commercial use is not permitted.

## Contact 📧

- **Author**: Manjushree
- **GitHub**: [manjushree08](https://github.com/manjushree08)
- **LinkedIn**: [Manju Shree](https://www.linkedin.com/in/manju-shree-1629b28a)
=======
This project is licensed for **Personal Use Only**. Redistribution or commercial use is not permitted.



## Contact 📧
- **Author**: Manjushree
- **GitHub**: [manjushree08](https://github.com/manjushree08)
- **LinkedIn**: [Manju Shree](https://www.linkedin.com/in/manju-shree-1629b28a)

>>>>>>> 26c5b7025d5092c082d1f178bbc75b42de82e756
