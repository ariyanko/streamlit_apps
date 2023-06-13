import streamlit as st
import pandas as pd

st.title('What to watch ?')
st.subheader('1000 movies 2006 - 2016')
'--------------'
movies=pd.read_csv('film.csv')
serch=st.radio('search type :',['title','filter'])

if serch=='title':
    userfilm=st.text_input('what is the name of the movie ? ')
    cons=movies['Title'].str.lower().str.contains(userfilm)

    
    
else:
    (shoro,payan)=st.slider('Year',
                            min_value=2006,
                            max_value=2016,
                            value=(2006,2016))
    cony=(movies['Year']>=shoro) & (movies['Year']<=payan)
    cons = cony
    
    rate=st.number_input('Rate',
                     min_value=1.0,
                     max_value=10.0,
                     step=0.5)
    conr=movies['Rating']>=rate
    cons = cons & conr
    def rep(string):
        return string.split(',')
    ganrlist=movies['Genre'].apply(rep)
    ganr=set()
    for i in ganrlist:
        for j in i:
            ganr.add(j.strip())
            
    userganr = st.multiselect('Genre', ganr)
    if len(userganr) >0:
       cong = movies['Genre'].str.contains(userganr[0])
       for k in userganr:
           cong = cong & movies['Genre'].str.contains(k)
       cons = cons & cong      


 
 
 
 
 
 
 
       
df=movies[cons]
if len(df)==1:
    st.write('A movie found')
elif len(df)==0:
    st.write('No movies found')
else:
    st.write(f'{len(df)} movies found')
df