
import streamlit as st 

nav2 = {
    
    "Study Options": [
        st.Page("korean_post5.py", title="Choices(Multiple)"),
        st.Page("listening-reading.py", title="Listening/Reading"),
        st.Page("Replicate_anki.py", title="Classic studying"),
        st.Page("stream_.py", title="Type-in"),
    ],
    "Other options": [
        st.Page("lookat_list.py", title="All lists"),
        st.Page("studyingphrases.py", title="Phrase's Definition"),
    ],
}

pg = st.navigation(nav2)
pg.run()