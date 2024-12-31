import streamlit as st
from All_Phrases.Japanese_Phrases.All_Japanese_ph import *
import random
import pandas as pd
st.markdown(
        """
    <style>
        
        
        div[role=radiogroup] label:first-of-type {
            visibility: hidden;
            height: 0px;
        }
        audio {
            filter: sepia(50%) saturate(80%) contrast(99%) invert(72%);
            width: 15px;
            height: 22px;
    
        }
    </style>
    """,
        unsafe_allow_html=True,
    )





if 'ao' not in st.session_state:
  st.session_state.ao = 0 


if 'd' not in st.session_state:
  st.session_state['d'] = 0


options:str = st.selectbox("Pick a list to study:",(
                                                


  f"1.1 {korean_useful_polite.getDefault_Name()}",#"1.6 korean useful polite words",
  f"2.1 {korean_particle_polite.getDefault_Name()}",#"2.6 korean particle polite words",
  f"3.1 {korean_past_polite2.getDefault_Name()}",#"3.6 korean past polite words 2",
  f"4.1 {korean_present_polite.getDefault_Name()}",#"4.6 korean present polite words",
  f"5.1 {korean_future_polite.getDefault_Name()}",#"5.6 korean future polite words",
  f"6.1 {korean_future_polite2.getDefault_Name()}",#"6.6 korean future polite words 2",
  f"7.1 {korean_past_polite.getDefault_Name()}",#"7.2 korean past polite words",
  ),index=None,placeholder="Select List")

if options != None or options == "":
  studying_list = []
  if (int(options[2])%2 != 0): 
    studying_list:list = All_korean_lists[int(str(options[0]))-1].de_ko_List
    
    #df1 = pd.DataFrame(studying_list)
    #st.write(df1)
  
  
  else:
    studying_list:list = list(All_words_korean[int(str(options[0]))-1]) 




    
    if 'no' not in st.session_state:
      st.session_state.no = False
    if 'rando_list' not in st.session_state:
      st.session_state.rando_list = [0,1,2,3]
    if 'rand_list' not in st.session_state:
      st.session_state.rand_list = [0,1,2,3]

  #if 'audio' not in st.session_state:
    #st.session_state.audio = All_Audio_korean
  #@st.cache_data
  #def show_():
    #st.audio(All_Audio_korean[3][st.session_state.ao],format="audio/wav")


  type_studying = st.radio("How do you want to study?:",["","Listening","Reading"])

  try:



    if type_studying == "Listening":
      #st.subheader(st.audio(All_Audio_korean[3][st.session_state.ao],format="audio/wav",autoplay=True))
        

      @st.cache_data
      def rand_List(n_phrases: int):

        st.session_state.rand_list = [None]*len(studying_list)
        for i in range(len(studying_list)):
            st.session_state.rand_list[i] = i
          #print(*rand_list)
        random.shuffle(st.session_state.rand_list)
          #print(*rand_list)
        st.session_state.rando_list = [st.session_state.rand_list[0],st.session_state.rand_list[1],st.session_state.rand_list[2]]
        st.session_state.rando_list.append(st.session_state.d)
        #print(*st.session_state.rando_list)
        random.shuffle(st.session_state.rando_list)
        return st.session_state.rando_list
        #print(*st.session_state.rando_list)
        


      def nextQuestion():
        st.session_state['d'] +=1
      st.divider()
    #a1 = studying_list[st.session_state.rando_list[0]][1]
    #a2 = studying_list[st.session_state.rando_list[1]][1]
    #a3 = studying_list[st.session_state.rando_list[2]][1]
      #a4 = studying_list[st.session_state.rando_list[3]][1]
  #try:

      
      
      

      st.write("Question:",str(st.session_state.d+1),"/",str(len(studying_list)))
      #if korean_present_polite.getDefault_Name() == "Korean Present Polite Speech:":
      st.audio(All_Audio_korean[3][st.session_state['d']], format="wav/audio")
      question = st.radio(f"What is the audio saying: ",[" ",studying_list[rand_List(st.session_state.d)[0]][0],studying_list[rand_List(st.session_state.d)[1]][0],studying_list[rand_List(st.session_state.d)[2]][0],studying_list[rand_List(st.session_state.d)[3]][0]])
      if studying_list[st.session_state.d][0] == question:
          st.success("Correct")

      elif " " == question:
          pass
      else:
          #st.write("Nope")


        st.error("Nope")
        
      st.button("->",on_click=nextQuestion)



    elif type_studying == "Reading":

      def next_phrase():
        st.session_state.ao +=1
      st.divider()
      st.write("Question:",str(st.session_state.ao + 1),"/",str(len(studying_list)))

      @st.cache_data
      def sub_t():
        st.subheader("Read the Korean phrase or word.")
      sub_t()
      st.subheader(studying_list[st.session_state.ao][0])



      def show_():
        st.audio(All_Audio_korean[3][st.session_state.ao],format="audio/wav",autoplay=True)



      if st.button("Show Answer:"):
        show_()
          #st.audio(st.session_state.audio[3][st.session_state.ao],format="audio/wav")



      st.button("->",on_click=next_phrase)
  except(IndexError):
    st.cache_data.clear()
    st.session_state.d = 0
    st.session_state.ao = 0
    st.rerun()
      


