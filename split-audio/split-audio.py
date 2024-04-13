from pydub import AudioSegment

def split_audio(file_path, segment_length=180000):
    """
    Split an audio file into segments of a given length.
    
    :param file_path: Path to the input audio file.
    :param segment_length: Length of each segment in milliseconds (default: 180000 for 3 minutes).
    """
    # Load the audio file
    audio = AudioSegment.from_file(file_path)
    
    # Calculate the number of segments needed
    total_length = len(audio)
    num_segments = total_length // segment_length + (1 if total_length % segment_length > 0 else 0)
    
    # Split and export the segments
    for i in range(num_segments):
        start_time = i * segment_length
        end_time = min((i + 1) * segment_length, total_length)
        segment = audio[start_time:end_time]
        segment.export(f"{file_path}_segment_{i+1}.mp3", format="mp3")

# Example usage
split_audio("audio.mp3")

