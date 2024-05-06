import cleanup
import smallvideos, finalvideo
import hangcsinalo
import szetszedes, karcolas
video_path = input("Background video path: \n")
url = input("reddit link: ")
words_to_split_at = input("words to split at SEPARATED BY SPACE: \n").split(" ")
subtitles_and_sounds_path = szetszedes.szetszedes(karcolas.szeddkiaszoveget(url),words_to_split_at)
input("press enter after revising split.txt")
hangcsinalo.hangkeszites(subtitles_and_sounds_path) #only german voice because i didnt find english 
smallvideos.makeVids('BgVid2.mp4','split.txt','hang') #change bigvid2.mp4 to your background video :) 
finalvideo.concatenate_videos(finalvideo.getVideoFiles("Videos"), 'output.mp4')

cleanup.RemoveFolder('hang')
cleanup.RemoveFolder('Videos')
cleanup.RemoveFile('saved.txt')
cleanup.RemoveFile("split.txt")

#words to split at for german
# ["und", "sondern", "oder", "dann", "aber", "trotzdem", "weil", "ob", "obwohl", "denn", "dass"]


# found tts models :)

#  1: tts_models/multilingual/multi-dataset/xtts_v2
#  2: tts_models/multilingual/multi-dataset/xtts_v1.1
#  3: tts_models/multilingual/multi-dataset/your_tts
#  4: tts_models/multilingual/multi-dataset/bark
#  10: tts_models/en/ek1/tacotron2
#  11: tts_models/en/ljspeech/tacotron2-DDC
#  12: tts_models/en/ljspeech/tacotron2-DDC_ph
#  13: tts_models/en/ljspeech/glow-tts
#  14: tts_models/en/ljspeech/speedy-speech
#  15: tts_models/en/ljspeech/tacotron2-DCA
#  16: tts_models/en/ljspeech/vits
#  17: tts_models/en/ljspeech/vits--neon
#  18: tts_models/en/ljspeech/fast_pitch
#  19: tts_models/en/ljspeech/overflow
#  20: tts_models/en/ljspeech/neural_hmm
#  21: tts_models/en/vctk/vits
#  22: tts_models/en/vctk/fast_pitch
#  23: tts_models/en/sam/tacotron-DDC
#  24: tts_models/en/blizzard2013/capacitron-t2-c50
#  25: tts_models/en/blizzard2013/capacitron-t2-c150_v2
#  26: tts_models/en/multi-dataset/tortoise-v2
#  27: tts_models/en/jenny/jenny
#  28: tts_models/es/mai/tacotron2-DDC
#  29: tts_models/es/css10/vits
#  32: tts_models/uk/mai/glow-tts
#  33: tts_models/uk/mai/vits
#  53: tts_models/hu/css10/vits


#  Name format: type/language/dataset/model
#  1: vocoder_models/universal/libri-tts/wavegrad
#  2: vocoder_models/universal/libri-tts/fullband-melgan
#  3: vocoder_models/en/ek1/wavegrad
#  4: vocoder_models/en/ljspeech/multiband-melgan
#  5: vocoder_models/en/ljspeech/hifigan_v2
#  7: vocoder_models/en/blizzard2013/hifigan_v2
#  8: vocoder_models/en/vctk/hifigan_v2
#  9: vocoder_models/en/sam/hifigan_v2