from pydub import AudioSegment

# 45 split c: 73 113
10,11,12
to_combine = [0,4,13,18]

for i in to_combine:
     
    # Load the WAV files
  sound1 = AudioSegment.from_mp3(fr"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases\Audio_file_korean_present_polite\chunk{10}.mp3")
  sound2 = AudioSegment.from_mp3(fr"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases\Audio_file_korean_present_polite\chunk{11}.mp3")
  sound3 = AudioSegment.from_mp3(fr"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases\Audio_file_korean_present_polite\chunk{12}.mp3")

    # Combine the WAV files
  combined_sound = sound1 + sound2 + sound3
    # Export the combined WAV file
  combined_sound.export(fr"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases\Audio_file_korean_present_polite\{0}chunk{8}.mp3", format="mp3") 


