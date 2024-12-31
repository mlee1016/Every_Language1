from pydub import AudioSegment
from pydub.silence import split_on_silence

sound = AudioSegment.from_file("korean_phrases_\korean_present_polite.mp3")

chunks = split_on_silence(sound, 
                          
    min_silence_len=200,
    silence_thresh=-20, 
    keep_silence=True
)

for i, chunk in enumerate(chunks):
    chunk.export(fr"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\Audio_present_korean\chunk{i+50}.mp3", format="mp3")