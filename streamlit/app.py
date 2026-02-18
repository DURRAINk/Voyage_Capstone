import streamlit as st
import joblib

hotel_map ={0: 'Hotel A', 1: 'Hotel AF', 2: 'Hotel AU', 3: 'Hotel BD', 4: 'Hotel BP',
             5: 'Hotel BW', 6: 'Hotel CB', 7: 'Hotel K', 8: 'Hotel Z'}
places = ['Florianopolis (SC)', 'Salvador (BH)', 'Natal (RN)',
       'Aracaju (SE)', 'Recife (PE)', 'Sao Paulo (SP)',
       'Campo Grande (MS)', 'Rio de Janeiro (RJ)', 'Brasilia (DF)']
rec_model = joblib.load('../models/hotel_recommendation_model/model.pkl')

# App title
st.title("🏨 Hotel Recommendation System")

# Input fields
place = st.selectbox("Select the place you want to visit:", places)
days = st.number_input("Enter number of days to stay:", min_value=1, step=1)

# Button to trigger recommendation
if st.button("Get Recommendation"):
    if place and days:
        prediction = rec_model.predict({'place': place, 'days': days})
        hotel_name = hotel_map[prediction[0]] if prediction[0] in hotel_map else "Unknown Hotel"
        
        st.success(f"Recommended Hotel for {place} ({days} days): **{hotel_name}**")
    else:
        st.warning("Please provide both place and days.")
