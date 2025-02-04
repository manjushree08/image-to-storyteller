from flask import Flask, render_template, request, send_file
import os
import generateStory

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if "image" not in request.files:
        return "No file uploaded", 400

    image = request.files["image"]
    if image.filename == "":
        return "No selected file", 400

    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(filepath)
    image_path = filepath 

    #helper methods to generate the story
    caption = generateStory.generate_image_to_text(image_path)
    story = generateStory.generate_text_to_story(caption)
    audio = generateStory.generate_story_to_audio(story,UPLOAD_FOLDER)


    audio_path = os.path.join(UPLOAD_FOLDER, "audio.wav")
    return {"story": story, "audio": "/play_audio"}

@app.route("/play_audio")
def play_audio():
    return send_file(os.path.join(UPLOAD_FOLDER, "audio.wav"), mimetype="audio/wav")

if __name__ == "__main__":
    app.run(debug=True)
