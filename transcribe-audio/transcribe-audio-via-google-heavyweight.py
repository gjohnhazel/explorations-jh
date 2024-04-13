import speech_recognition as sr
import math
import os

def transcribe_large_audio(file_path, output_path):
    # Initialize recognizer class (for recognizing the speech)
    recognizer = sr.Recognizer()

    # Open the audio file using pydub
    try:
        from pydub import AudioSegment
        audio = AudioSegment.from_wav(file_path)
    except ImportError:
        print("Please install pydub: pip install pydub")
        return

    # Break audio into chunks of 1 minute or less
    chunk_length_ms = 60000  # pydub calculates in millisec
    chunks = [audio[i:i + chunk_length_ms] for i in range(0, len(audio), chunk_length_ms)]
    folder_name = "audio-chunks"
    # Create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    
    # Process each chunk 
    for i, chunk in enumerate(chunks, start=1):
        chunk_file = os.path.join(folder_name, f"chunk{i}.wav")
        chunk.export(chunk_file, format="wav")
        # Load the audio file
        with sr.AudioFile(chunk_file) as source:
            audio_listened = recognizer.record(source)
            # Try to recognize the speech in the chunk
            try:
                print(f"Transcribing chunk {i}...")
                text = recognizer.recognize_google(audio_listened)
            except sr.UnknownValueError:
                text = "[Inaudible]"
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                return

            # Append the text of each chunk to the file
            with open(output_path, 'a') as out_file:
                out_file.write(text + '\n')

    print(f"Transcription saved to {output_path}")

# Set paths to your audio file and output text file
audio_path = "audio.wav"
output_path = "transcript-google.txt"

# Transcribe the audio
transcribe_large_audio(audio_path, output_path)
