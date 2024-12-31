import streamlit as st


st.subheader("Study Languages - Phrases")
nav2 = {
    
    "Lanuages": [
        st.Page("all.py", title="Korean"),
        st.Page("Russian_all.py", title="Russian"),
        st.Page("Italian_all.py", title="Italian"),
        st.Page("German_all.py", title="German"),
    
        st.Page("Japanese_all.py", title="Japanese"),]
        
}

pg = st.navigation(nav2)
pg.run()
