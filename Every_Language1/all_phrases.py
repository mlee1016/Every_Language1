import streamlit as st



nav2 = {


    
    "1) KOREAN Study Options-------        ": [
        st.Page("korean_post5.py", title="Choices(Multiple)"),
        st.Page("listening-reading.py", title="Listening/Reading"),
        st.Page("Replicate_anki.py", title="Classic studying"),
        st.Page("stream_.py", title="Type-in"),
    ],
    "Other options": [
        st.Page("lookat_list.py", title="All lists"),
        st.Page("studyingphrases.py", title="Phrase's Definition"),

    ],
  
    "2) RUSSIAN Study Options----        ": [
        st.Page("Russia_post5.py", title="Choices(Multiple)"),
        st.Page("russian_listening-reading copy.py", title="Listening/Reading"),
        st.Page("Russian_Replicate_anki_copy.py", title="Classic studying"),
        st.Page("russian_stream_copy.py", title="Type-in"),
    ],
    "Other options": [
        st.Page("russian_lookat_listcopy.py", title="All lists"),
        st.Page("russian_studyingphrasescopy.py", title="Phrase's Definition"),

    ],
    
    "3) ITALIAN Study Options               ": [
        st.Page("Italian_post5.py", title="Choices(Multiple)"),
        st.Page("I_listening-reading.py", title="Listening/Reading"),
        st.Page("I_Replicate_anki.py", title="Classic studying"),
        st.Page("I_stream_.py", title="Type-in"),
    ],
    "Other options": [
        st.Page("I_lookat_list.py", title="All lists"),
        st.Page("I_studyingphrases.py", title="Phrase's Definition"),

    ],
    
    "4) JAPANESE Study Options                ": [
        st.Page("Japanese_post5.py", title="Choices(Multiple)"),
        st.Page("J_listening-reading.py", title="Listening/Reading"),
        st.Page("J_Replicate_anki.py", title="Classic studying"),
        st.Page("J_stream_.py", title="Type-in"),
    ],
    "Other options": [
        st.Page("J_lookat_list.py", title="All lists"),
        st.Page("J_studyingphrases.py", title="Phrase's Definition"),

    ],
    
    
    "5) GERMAN Study Options": [
        st.Page("German_post5.py", title="Choices(Multiple)"),
        st.Page("g_listening-reading.py", title="Listening/Reading"),
        st.Page("g_Replicate_anki.py", title="Classic studying"),
        st.Page("g_stream_.py", title="Type-in"),
    ],
    "Other options": [
        st.Page("g_lookat_list.py", title="All lists"),
        st.Page("g_studyingphrases.py", title="Phrase's Definition"),

    ],




}

pg = st.navigation(nav2)
pg.run()

