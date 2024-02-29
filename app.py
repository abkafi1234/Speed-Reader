import time 
import streamlit as st
from PyPDF2 import PdfReader 

st.title("Speed Reader")
file = st.file_uploader('Please upload the PDF file')
if file:
    values = st.slider('Please Enter Word per Second you want to try:', 5, 20, 5)

    reader = PdfReader(file)
    for i in range(1, len(reader.pages)):
        pages = reader.pages[i]
        text = pages.extract_text()
        #
        placeholder = st.empty()
        starttime = time.time()
        passedtime = 0
        for i in text.split():
            with placeholder.container():
                st.markdown(f'## {i}')
            time.sleep(1/values)
            passedtime += time.time() - starttime
            if passedtime % 3 == 0:
                values += 2
            placeholder.empty()
