import csv
import pandas as pd
import copy
from all_audio_russian import *
default_Ru_Ph = [[] for i in range(7)]

with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\russian_phrases\russian_ph.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ru_Ph[0] = list(reader)



with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\russian_phrases\Russian_prepositional.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ru_Ph[1] = list(reader)



with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\russian_phrases\Russian_Instrumental.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ru_Ph[2] = list(reader)



with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\russian_phrases\russian_dative.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ru_Ph[3] = list(reader)



with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\russian_phrases\Russian_acusative.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ru_Ph[4] = list(reader)



with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\russian_phrases\Russian_nominative.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_Ru_Ph[5] = list(reader)










#print(len(default_Ru_Ph))


#list_15_ru = [default_Ru_Ph[y:y+15] for y in range(0,len(default_Ru_Ph),15)]
#print(len(list_15_ru[8]))




class Russian():
    # cu = custom / ru = russian / de = default 
    de_ru_List = []
    de_ru_name = ""
    cu_ru_List = []
    cu_ru_name = ""
    se_ = 0
    def __init__(self,r_name:str,ru_list):
        self.de_ru_List = ru_list
        self.de_ru_name = r_name
        Russian.se_ += 1
    def customRuList(self, c_r_name, c_ru_List):
        self.cu_ru_List = c_ru_List
        self.cu_ru_name = c_r_name
    def getCustom_Name(self) -> str:
        return self.cu_ru_name
    def getDefault_Name(self) -> str:
        return self.de_ru_name
    
    def getList(self,name:str):
        if self.de_ru_name == name:
            return self.de_ru_List
        return []
    def return_ie():
        return Russian.se_
   
Russian_useful_polite = Russian("Russian Useful Phrases:",copy.deepcopy(default_Ru_Ph[0]))

#print(len(Russian_useful_polite.de_ru_List[0]))
#print(len(korean_present_polite.de_ko_List))

russian_present_polite_words = set()
str_kp1 = []
col_1 = []
for r in range(len(Russian_useful_polite.de_ru_List)):
    col_1.append(Russian_useful_polite.de_ru_List[r][0])


for i in range(len(col_1)):
  str_kp1.extend(col_1[i].split())
for d in range(len(str_kp1)):
    russian_present_polite_words.add(str_kp1[d])

print(1, len(russian_present_polite_words))

russian_prepositional_polite = Russian("Russian Prepositional Polite Speech:",copy.deepcopy(default_Ru_Ph[1]))
#print(len(korean_past_polite.de_ko_List))

russian_p_polite_words = set()
str_kp2 = []
col_o2 = []

for s in range(len(russian_prepositional_polite.de_ru_List)):
    col_o2.append(russian_prepositional_polite.de_ru_List[s][0])


for i in range(len(col_o2)):
  str_kp2.extend(col_o2[i].split())
for d in range(len(str_kp2)):
    russian_p_polite_words.add(str_kp2[d])
#print(len(str_kp2))
print(2, len(list(russian_p_polite_words)))


russian_Instrumental_polite = Russian("Russian Instrumental Polite Speech: ",copy.deepcopy(default_Ru_Ph[2]))
#print(len(korean_future_polite.de_ko_List))
#print(korean_future_polite.de_ko_List[1][0])

russian_I_polite_words = set()
str_kp3 = []
col_o3 = []


for s in range(len(russian_Instrumental_polite.de_ru_List)):
    col_o3.append(russian_Instrumental_polite.de_ru_List[s][0])



for i in range(len(col_o3)):
  str_kp3.extend(col_o3[i].split())
for d in range(len(str_kp3)):
    russian_I_polite_words.add(str_kp3[d])
#print(len(str_kp3))
print(3, len(list(russian_I_polite_words)))

Russian_dative_polite = Russian("Russian Dative Polite Speech: ",copy.deepcopy(default_Ru_Ph[3]))
#print(len(korean_past_polite2.de_ko_List))

russian_d_polite_words = set()
str_kp4 = []
col_o4 = []


for s in range(len(Russian_dative_polite.de_ru_List)):
    col_o4.append(Russian_dative_polite.de_ru_List[s][0])


for i in range(len(col_o4)):
  str_kp4.extend(col_o4[i].split())
for d in range(len(str_kp4)):
    russian_d_polite_words.add(str_kp4[d])

#print(len(str_kp4))
print(4, len(list(russian_d_polite_words)))

russian_accusative_polite = Russian("Russian accusative Polite Speech: ",copy.deepcopy(default_Ru_Ph[4]))
#print(len(korean_future_polite2.de_ko_List))

r_a_polite2_words = set()
str_kp5 = []
col_o5 = []


for s in range(len(russian_accusative_polite.de_ru_List)):
    col_o5.append(russian_accusative_polite.de_ru_List[s][0])


for i in range(len(col_o5)):
  str_kp5.extend(col_o5[i].split())
for d in range(len(str_kp5)):
    r_a_polite2_words.add(str_kp5[d])
#print(len(str_kp5))
print(5, len(list(r_a_polite2_words)))

Russian_nominative_polite = Russian("Russian nominative Phrases: ",copy.deepcopy(default_Ru_Ph[5]))
#print(len(korean_useful_polite.de_ko_List))


r_n_polite_words = set()
str_kp6 = []
col_o6 = []


for e in range(len(Russian_nominative_polite.de_ru_List)):
    col_o6.append(Russian_nominative_polite.de_ru_List[e][0])


for i in range(len(col_o6)):
  str_kp6.extend(col_o6[i].split())
for d in range(len(str_kp6)):
    r_n_polite_words.add(str_kp6[d])
#print(len(str_kp6))
print(6, len(list(r_n_polite_words)))

#russian_particle_polite = Russian("Korean Particle Phrases: ",copy.deepcopy(default_Ru_Ph[6]))
#print(len(korean_particle_polite.de_ko_List))


#russian_particle_polite_words = set()
#str_kp7 = []
#col_o7 = []




#for t in range(len(russian_particle_polite.de_ru_List)):
    #col_o7.append(russian_particle_polite.de_ru_List[t][0])


#for i in range(len(col_o7)):
  #str_kp7.extend(col_o7[i].split())
#for d in range(len(str_kp7)):
    #russian_particle_polite_words.add(str_kp7[d])
#print(len(str_kp7))
#print(7, len(list(russian_particle_polite_words)))




All_russian_lists = [Russian_nominative_polite,russian_accusative_polite,Russian_useful_polite,
russian_Instrumental_polite,russian_prepositional_polite,Russian_dative_polite]

All_words_russian = [r_a_polite2_words,r_n_polite_words,
russian_present_polite_words,russian_p_polite_words,russian_I_polite_words,russian_d_polite_words]






All_Audio_russian = [None]*len(All_russian_lists)

#All_Audio_russian[0] = russian_n

#All_Audio_russian[1] = russian_ueful
#All_Audio_russian[2] = russian_a
All_Audio_russian[3] = russian_i
All_Audio_russian[4] = russian_p
All_Audio_russian[5] = russian_d
from gtts import *




#for i in range(len(russian_preposional_polite.de_ru_List)):



    #tts = gTTS(russian_preposional_polite.de_ru_List[i][0], lang='ru')
    #tts.save(fr"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\russian_phrases\Russian_Pre_audio\Russian_pre{i}.mp3")
