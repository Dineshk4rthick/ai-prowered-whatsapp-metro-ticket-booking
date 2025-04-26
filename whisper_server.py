from flask import Flask, request, jsonify
import whisper
import os
import tempfile

app = Flask(__name__)

print("Loading Whisper model... this may take a minute...")
# Load the Whisper model (tiny is fastest, base is good balance, medium/large are most accurate)
model = whisper.load_model("base")
print("Whisper model loaded! Server ready.")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    file = request.files["audio"]
    
    # Create a temporary file with the correct extension
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, "temp_audio.ogg")
    
    try:
        file.save(temp_path)
        print(f"Audio saved to {temp_path}, starting transcription...")
        
        # Transcribe the audio
        result = model.transcribe(temp_path)
        transcribed_text = result["text"].strip()
        print(f"Transcription result: {transcribed_text}")
        
        # Return the transcribed text
        return jsonify({"text": transcribed_text})
    
    except Exception as e:
        print(f"Error during transcription: {str(e)}")
        return jsonify({"error": str(e)}), 500
    
    finally:
        # Clean up the temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    print("Starting Whisper transcription server on port 5001...")
    app.run(host="0.0.0.0", port=5001, debug=True)
