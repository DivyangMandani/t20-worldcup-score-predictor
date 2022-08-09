import streamlit as st
import pandas as pd
import numpy as np
import pickle

pipe=pickle.load(open('pipe.pkl','rb'))

teams=[
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'
]

city=[
    'Durban', 'Mumbai', 'Cape Town', 'Pallekele', 'Auckland',
    'Abu Dhabi', 'Chandigarh', 'Mirpur', 'London', 'Barbados',
    'Centurion', 'Delhi', 'Cardiff', 'Melbourne', 'St Kitts',
    'Johannesburg', 'Colombo', 'Dubai', 'Nagpur', 'Sydney',
    'Chittagong', 'Nottingham', 'Hamilton', 'Kolkata', 'Lauderhill',
    'Bangalore', 'St Lucia', 'Manchester', 'Wellington', 'Southampton',
    'Adelaide', 'Christchurch', 'Mount Maunganui', 'Lahore',
    'Trinidad'
]

st.title('Cricket Score Predictor')

col1,col2=st.columns(2)

with col1:
    batting_team=st.selectbox('Select Batting Team',sorted(teams))

with col2:
    bowling_team=st.selectbox('Select Bowling Team',sorted(teams))   

city=st.selectbox('Select City',sorted(city))

col3,col4,col5=st.columns(3)

with col3:
    current_score=st.number_input('Enter Current Score')

with col4:
    wickets=st.number_input('Wickets Out')  

with col5:
    overs=st.number_input('Overs done (Work for over>5)')      

last_five=st.number_input('Runs Score in Last 5 Overs')

if st.button('Predict'):
    balls_left=120-(overs*6)
    wickets_left=10-wickets
    crr=current_score/overs

    input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[city],'current_score':[current_score],'balls_left':[balls_left],'wickets_left':[wickets_left],'crr':[crr],'last_five':[last_five]})

    predected_score=pipe.predict(input_df)
    predected_score_int=int(predected_score[0])
    st.header("Predicted Score - " + str(predected_score_int) + " " +"runs")