import speech_recognition as sr

def transcribe_audio(audio_path, output_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)

    try:
        # Transcribe audio using Google Web Speech API
        print("Transcribing audio...")
        text = recognizer.recognize_google(audio_data)
        print("Transcription Successful! Writing to file...")
        # Write transcription to file
        with open(output_file, 'w') as file:
            file.write(text)
        print(f"Transcript saved to {output_file}")
    except sr.UnknownValueError:
        print("Google Web Speech API could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

# Path to your WAV file and output txt file
audio_path = "audio-1.WAV"
output_file = "transcript-1.txt"

# Call the function
transcribe_audio(audio_path, output_file)
