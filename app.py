import streamlit as st
try:
 from pypdf import PdfReader
except: PdfReader=None
st.title('MBA SWAYAM Agent MVP')
f=st.file_uploader('Upload syllabus PDF',type='pdf')
fee=st.selectbox('Fee',['Free','<=500','<=1000','No limit'])
hrs=st.slider('Weekly hours',1,15,6)
if f:
 st.success('Syllabus uploaded')
 if PdfReader:
  try:
   t=''.join((p.extract_text() or '') for p in PdfReader(f).pages)
   st.text(t[:1000])
  except Exception: pass
 if st.button('Recommend'):
  st.write([{'Course':'Business Analytics','Score':92,'Fee':fee,'Hours':hrs},
            {'Course':'AI for Managers','Score':88,'Fee':'Free','Hours':6}])
