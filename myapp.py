import streamlit as st
import numpy as np
import pandas as pd

st.title("hello streamlit")
st.write("this is your first streamlit app")
st.text("lets get started")


df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)



# media layout 
st.sidebar.title("Navigation")
st.image("https://www.bing.com/images/search?view=detailV2&ccid=qtNzEsgf&id=207BC46E764FB2CD96D2E811508374CF870D9664&thid=OIP.qtNzEsgfaGzcXbwcScXAHAHaE0&mediaurl=https%3a%2f%2fgyaanarth.com%2fwp-content%2fuploads%2f2022%2f05%2fabout_ycce.jpg&exph=325&expw=500&q=ycce+image&mode=overlay&FORM=IQFRBA&ck=440FCC91C498A5C184DF69DB42D21A93&selectedIndex=0&idpp=serp" , caption="sample image")
st.video("https://youtu.be/Pcgoe67_nxk")

# csv file 
upload_file=st.file_uploader(" ",type='csv')
if upload_file:
    df=pd.read_csv(upload_file)
    st.dataframe(df)
    
st.code("for i in range(5): print(i)",language="python")
st.text_input("what is your name ")
st.text_area("write something")
st.number_input("Enter number")
st.slider("choose a range ",0,100)
st.selectbox("select a fruit" ,["Apple" ,"Banana" , "Mango"])
st.multiselect("choose toppings ",["Apple" ,"Banana" , "Mango"])
st.radio("pick one ",["A","B","C"])
st.checkbox("I agree the terms")



if st.checkbox("show Details"):
    st.info("Here are more details ")
option=st.radio("choose a view ",["Show chart","show table"])
if option=="show chart":
    st.write("chart would appear here")
else:
    st.write("table would appear here")


with st.form("login_form"):
    username=st.text_input("Username")
    password=st.text_input("password" , type="password")
    submitted=st.form_submit_button("login")
    
    if submitted:
        st.success(f"welcome , {username}!")
