import os
import speech_recognition as sr
from rake_nltk import Rake
import nltk 
from nltk.corpus import wordnet 
synonyms = [] 
antonyms = [] 
available_adds = ["algorithm course","learn sorting algorithm","hotel reservation","car launch","world cricket championship","jigsaw sports academy"]
pyscene_detect = "scenedetect -i algorithm.mp4 detect-content -t 50 list-scenes split-video"
os.system(pyscene_detect)
command2mp3 = "ffmpeg -i algorithm.mp4 algorithm.mp3 -y"
command2wav = "ffmpeg -i algorithm.mp3 algorithm.wav -y"
os.system(command2mp3)
os.system(command2wav)
r = sr.Recognizer()
audio = sr.AudioFile('algorithm.wav')
with audio as source:
	audio = r.record(source)
video_text = r.recognize_google(audio)
rake_result = []
final_rake_res = []
ra = Rake()
ra.extract_keywords_from_text(video_text)
rake_result = ra.get_ranked_phrases()
#print(ra.get_ranked_phrases_with_scores())
#print(rake_result)
for word in rake_result:
	length = len(word.split())
	if length == 1:
		final_rake_res.append(word)
print("\n Final Rake output")
print(final_rake_res)
for i in range(len(final_rake_res)):
	for syn in wordnet.synsets(final_rake_res[i]): 
    		for l in syn.lemmas(): 
        		synonyms.append(l.name()) 
        		if l.antonyms(): 
            			antonyms.append(l.antonyms()[0].name()) 
	#print(set(synonyms))

add_suggestion = []
res = ""
for word in final_rake_res:
	for add in available_adds:
		res = add.find(word)
		if res !=-1:
			if add in add_suggestion:
				continue
			else:
				add_suggestion.append(add)


res = ""
for add in available_adds:
	for i in range(len(final_rake_res)):
		for syn_word in synonyms[i]:
			if len(syn_word)>2:
				syn_res = add.find(syn_word)
				if syn_res != -1:
					if add in add_suggestion:
						continue
					else:
						add_suggestion.append(add)

		
print("\nADD SUGGESTION \n")
print(add_suggestion)
print("\n")
print("\n")



 




