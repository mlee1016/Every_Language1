
import streamlit as st 

nav2 = {
    
    "Study Options": [
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