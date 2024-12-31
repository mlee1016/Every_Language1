
import streamlit as st 

nav2 = {
    
    "Study Options": [
        st.Page("Italian_post5.py", title="Choices(Multiple)"),
        st.Page("I_listening-reading.py", title="Listening/Reading"),
        st.Page("I_Replicate_anki.py", title="Classic studying"),
        st.Page("I_stream_.py", title="Type-in"),
    ],
    "Other options": [
        st.Page("I_lookat_list.py", title="All lists"),
        st.Page("I_studyingphrases.py", title="Phrase's Definition"),
    ],
}

pg = st.navigation(nav2)
pg.run()