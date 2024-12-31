
import csv

default_It_Ph = []
with open(r'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\Italian_phrases\Italian_useful_phrases.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    default_It_Ph = list(reader)


    

#print(len(default_It_Ph))

class Italian():
    # cu = custom / ru = russian / de = default 
    de_it_List = []
    de_it_name = ""
    cu_it_List = []
    cu_it_name = ""
    se_ = 0
    def __init__(self,i_name:str,it_list):
        self.de_it_List = it_list
        self.it_name = i_name
        Italian.se_ += 1
    def customRuList(self, c_i_name, c_it_List):
        self.cu_ru_List = c_it_List
        self.cu_ru_name = c_i_name
    def getCustom_Name(self) -> str:
        return self.cu_it_name
    def getDefault_Name(self) -> str:
        return self.de_it_name
    
    def getList(self,name:str):
        if self.de_it_name == name:
            return self.de_it_List
        return []
    def return_ie():
        return Italian.se_
   

Italian_useful = Italian("Italian useful",default_It_Ph)

#from gtts import *
#print(len(Italian_useful.de_it_List))
#for i in range(len(Italian_useful.de_it_List)):



    #tts = gTTS(Italian_useful.de_it_List[i][0], lang='it')
    #tts.save(fr"C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\Italian_phrases\Italian_phrases_audio\italian_useful{i}.mp3")


Italian_audio = list()
for i in range(0,30):

  Italian_audio.append(fr'C:\Users\Owner\OneDrive\Desktop\css-HTML\open-project\Italian_phrases\Italian_phrases_audio\italian_useful{i}.mp3')

for i in  range(len(Italian_useful.de_it_List)):
    print(Italian_useful.de_it_List[i][0])

