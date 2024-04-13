from vosk import Model, KaldiRecognizer
import wave
import json
import os

def transcribe_audio(file_path, model_path, output_path):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Load the Vosk model
    model = Model(model_path)

    # Open the audio file
    with wave.open(file_path, "rb") as wf:
        # Create a recognizer with the model and audio file's sample rate
        rec = KaldiRecognizer(model, wf.getframerate())
        
        # Open output file
        with open(output_path, 'w') as out_file:
            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                if rec.AcceptWaveform(data):
                    # Process partial results
                    part_result = json.loads(rec.Result())
                    print(part_result.get('text', ''), file=out_file)
            # Process final result
            final_result = json.loads(rec.FinalResult())
            print(final_result.get('text', ''), file=out_file)

    print(f"Transcription saved to {output_path}")

# Set paths to your audio file and Vosk model directory
audio_path = "audio-1.WAV"
model_path = 'vosk-model-en-us-0.42-gigaspeech'
output_path = "transcript-1.txt"

# Transcribe the audio
transcribe_audio(audio_path, model_path, output_path)
