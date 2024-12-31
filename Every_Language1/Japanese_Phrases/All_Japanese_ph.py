import csv
import copy
#from audio_ko import ko_polite_present, ko_polite_useful
default_Ko_Ph = [[] for i in range(7)]
with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\korean_present_polite.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[0] = list(reader)
with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\korean_past_polite.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[1] = list(reader)


with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\korean_future_polite.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[2] = list(reader)

with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\korean_past_polite2.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[3] = list(reader)
with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\korean_future_polite2.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[4] = list(reader)


with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\korean_useful_phrases.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[5] = list(reader)


with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\korean_grammar_particle.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ko_Ph[6] = list(reader)

#print(default_Ko_Ph)


#list_15_ko = [default_Ko_Ph[y:y+15] for y in range(0,len(default_Ko_Ph),15)]
#print(list_15_ko[0])


class Korean():
    # cu = custom / ko = korean/ de = default 
    de_ko_List = []
    de_ko_name = ""
    cu_ko_List = []
    cu_ko_name = ""
    se_ = 0
    def __init__(self,k_name:str,ko_list):
        self.de_ko_List = ko_list
        self.de_ko_name = k_name
        Korean.se_ +=1
    def customRuList(self, k_r_name, k_ru_List):
        self.ko_ru_List = k_ru_List
        self.ko_ru_name = k_r_name
    def getCustom_Name(self) -> str:
        return self.cu_ko_name
    def getDefault_Name(self) -> str:
        return self.de_ko_name
    
    def getList(self,name:str):
        if self.de_ko_name == name:
            return self.de_ko_List
        return []
    def return_ie():
        return Korean.se_
korean_present_polite = Korean("Korean Present Polite Speech: ",copy.deepcopy(default_Ko_Ph[0]))
#print(len(korean_present_polite.de_ko_List))

korean_present_polite_words = set()
str_kp = []
col_ = []
for s in range(len(korean_present_polite.de_ko_List)):
    col_.append(korean_present_polite.de_ko_List[s][0])


for i in range(len(col_)):
  str_kp.extend(col_[i].split())
for d in range(len(str_kp)):
    korean_present_polite_words.add(str_kp[d])

print(1, len(korean_present_polite_words))

korean_past_polite = Korean("Korean Past Polite Speech: ",copy.deepcopy(default_Ko_Ph[1]))
#print(len(korean_past_polite.de_ko_List))

korean_past_polite_words = set()
str_kp2 = []
col_o2 = []

for s in range(len(korean_past_polite.de_ko_List)):
    col_o2.append(korean_past_polite.de_ko_List[s][0])


for i in range(len(col_o2)):
  str_kp2.extend(col_o2[i].split())
for d in range(len(str_kp2)):
    korean_past_polite_words.add(str_kp2[d])
#print(len(str_kp2))
print(2, len(list(korean_past_polite_words)))


korean_future_polite = Korean("Korean Future Polite Speech: ",copy.deepcopy(default_Ko_Ph[2]))
#print(len(korean_future_polite.de_ko_List))
#print(korean_future_polite.de_ko_List[1][0])

korean_future_polite_words = set()
str_kp3 = []
col_o3 = []


for s in range(len(korean_future_polite.de_ko_List)):
    col_o3.append(korean_future_polite.de_ko_List[s][0])



for i in range(len(col_o3)):
  str_kp3.extend(col_o3[i].split())
for d in range(len(str_kp3)):
    korean_future_polite_words.add(str_kp3[d])
#print(len(str_kp3))
print(3, len(list(korean_future_polite_words)))

korean_past_polite2 = Korean("Korean Past Polite Speech 2: ",copy.deepcopy(default_Ko_Ph[3]))
#print(len(korean_past_polite2.de_ko_List))

korean_past_polite2_words = set()
str_kp4 = []
col_o4 = []


for s in range(len(korean_past_polite2.de_ko_List)):
    col_o4.append(korean_past_polite2.de_ko_List[s][0])


for i in range(len(col_o4)):
  str_kp4.extend(col_o4[i].split())
for d in range(len(str_kp4)):
    korean_past_polite2_words.add(str_kp4[d])

#print(len(str_kp4))
print(4, len(list(korean_past_polite2_words)))

korean_future_polite2 = Korean("Korean Future Polite Speech2: ",copy.deepcopy(default_Ko_Ph[4]))
#print(len(korean_future_polite2.de_ko_List))

korean_future_polite2_words = set()
str_kp5 = []
col_o5 = []


for s in range(len(korean_future_polite2.de_ko_List)):
    col_o5.append(korean_future_polite2.de_ko_List[s][0])


for i in range(len(col_o5)):
  str_kp5.extend(col_o5[i].split())
for d in range(len(str_kp5)):
    korean_future_polite2_words.add(str_kp5[d])
#print(len(str_kp5))
print(5, len(list(korean_future_polite2_words)))

korean_useful_polite = Korean("Korean Useful Phrases: ",copy.deepcopy(default_Ko_Ph[5]))
#print(len(korean_useful_polite.de_ko_List))


korean_useful_polite_words = set()
str_kp6 = []
col_o6 = []


for s in range(len(korean_useful_polite.de_ko_List)):
    col_o6.append(korean_useful_polite.de_ko_List[s][0])


for i in range(len(col_o6)):
  str_kp6.extend(col_o6[i].split())
for d in range(len(str_kp6)):
    korean_useful_polite_words.add(str_kp6[d])
#print(len(str_kp6))
print(6, len(list(korean_useful_polite_words)))

korean_particle_polite = Korean("Korean Particle Phrases: ",copy.deepcopy(default_Ko_Ph[6]))
#print(len(korean_particle_polite.de_ko_List))


korean_particle_polite_words = set()
str_kp7 = []
col_o7 = []




for t in range(len(korean_particle_polite.de_ko_List)):
    col_o7.append(korean_particle_polite.de_ko_List[t][0])


for i in range(len(col_o7)):
  str_kp7.extend(col_o7[i].split())
for d in range(len(str_kp7)):
    korean_particle_polite_words.add(str_kp7[d])
#print(len(str_kp7))
print(7, len(list(korean_particle_polite_words)))




All_korean_lists = [korean_useful_polite,korean_particle_polite,korean_past_polite2,korean_present_polite,
korean_future_polite,korean_future_polite2,korean_past_polite]

All_words_korean = [korean_useful_polite_words,korean_particle_polite_words,korean_past_polite2_words,
korean_present_polite_words,korean_future_polite_words,korean_future_polite2_words,korean_past_polite_words]

All_Audio_korean = [None]*len(All_korean_lists)
All_Audio_korean[0] = ko_polite_useful
All_Audio_korean[3] = ko_polite_present

All_words_ = list(korean_useful_polite_words)+list(korean_particle_polite_words)+list(korean_past_polite2_words)+list(korean_present_polite_words)+list(korean_future_polite_words)+list(korean_future_polite2_words)+list(korean_past_polite_words)



from gtts import *

#for i in range(len(korean_useful_polite.de_ko_List)):

    #tts = gTTS(korean_useful_polite.de_ko_List[i][0], lang='ko')
    #tts.save(fr"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\korean_phrases_\korean_useful_{i}.mp3")
