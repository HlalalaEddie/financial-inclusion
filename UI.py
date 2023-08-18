import streamlit as st
import pickle

#Function to load the selected model
def load_model(model_name):
    model_path = f'{model_name}.pkl'
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def main():
  # Title of the web app
    st.title('Financial Inclusion In Africa')

    # Set custom CSS for the background image
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url('');
        background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    
    # Subheader
    st.subheader('Welcome! Select a model and input features for prediction.')

    # Dropdown to select the model
    model_options = ['XGBClassifier']
    selected_model = st.selectbox('Select Model', model_options)  

    # Load the selected model
    model = load_model(selected_model)

    # User input for features
    st.header('Feature Input')
    feature1 = st.number_input('location_type', value=0)
    feature2 = st.number_input('cellphone_access', value=0)
    feature3 = st.number_input('age_of_respondent', value=0)
    feature4 = st.number_input('education_level', value=0)
    feature5 = st.number_input('job_type', value=0)
 


    # Button for predictions
    clicked = st.button('Get Predictions')

    # Perform predictions when the button is clicked
    if clicked:
        # Perform predictions using the selected model
        prediction = model.predict([[feature1, feature2, feature3, feature4, feature5]])

        # Display the prediction result
        st.header('Prediction')
        st.write(f'The prediction result is:  {prediction[0]}')

if __name__ == '__main__':
    main()
