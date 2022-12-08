import streamlit as st
import numpy as np
import pandas as pd
import pickle
import lightgbm

pickled_scaler=pickle.load(open('C:/Users/RAM JAS/Documents/compressive strength/scaler.pkl', 'rb'))

pickled_model = pickle.load(open('C:/Users/RAM JAS/Documents/compressive strength/finalized_model.pkl', 'rb'))

def welcome():
    return "Welcome All"

def predict(cement, blast_furnace_slag, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age):

    #Predicting the price of the carat
    scaler_list=pickled_scaler.fit_transform([[cement, blast_furnace_slag, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age]]).tolist()

    prediction = pickled_model.predict(scaler_list)
        # pd.DataFrame(scaler_list,columns=
        # ["cement", "blast_furnace_slag", "fly_ash", "water", "superplasticizer","coarse_aggregate", "fine_aggregate", "age"]))    
    return prediction


def main():
    st.title('Compressive Strength Concrete Predictor')
    st.image("""https://civildigital.com/wp-content/uploads/2016/07/Hydraulic-Compression-Testing-Machine.jpg""")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Compressive Concrete Strength Predictor</h2>
    </div>
    """
    st.header('Enter the Components of Concrete') 

    st.markdown(html_temp,unsafe_allow_html=True)

    cement = st.number_input('cement:', min_value=50.0, max_value=1000.0, value=50.0)

    blast_furnace_slag = st.number_input('blast_furnace_slag:', min_value=0.1, max_value=400.0, value=1.0)

    fly_ash = st.number_input('fly_ash:', min_value=0.1, max_value=250.0, value=1.0)

    water = st.number_input('water:', min_value=100.0, max_value=250.0, value=100.0)

    superplasticizer = st.number_input('superplasticizer:', min_value=0.1, max_value=35.0, value=1.0)

    coarse_aggregate = st.number_input('Coarse_aggregates:', min_value=700.0, max_value=1200.0, value=700.0)

    fine_aggregate = st.number_input('Fine_aggregates:', min_value=500.0, max_value=1000.0, value=500.0)

    age = st.slider('Age in years:', min_value=0.1, max_value=400.0, value=1.0)
    # variance = st.text_input("Variance","Type Here")
    # skewness = st.text_input("skewness","Type Here")
    # curtosis = st.text_input("curtosis","Type Here")
    # entropy = st.text_input("entropy","Type Here")


    result=""
    
    # cement = st.number_input('cement:', min_value=0.1, max_value=10.0, value=1.0)

    # blast_furnace_slag = st.number_input('blast_furnace_slag:', min_value=0.1, max_value=100.0, value=1.0)

    # fly_ash = st.number_input('fly_ash:', min_value=0.1, max_value=100.0, value=1.0)

    # water = st.number_input('water:', min_value=0.1, max_value=100.0, value=1.0)

    # superplasticizer = st.number_input('superplasticizer:', min_value=0.1, max_value=100.0, value=1.0)

    # coarse_aggregate = st.number_input('Coarse_aggregates:', min_value=0.1, max_value=100.0, value=1.0)

    # fine_aggregate = st.number_input('Fine_aggregates:', min_value=0.1, max_value=100.0, value=1.0)

    # age = st.slider('Age in years:', min_value=0.5, max_value=150.0, value=1.0)


    # st.title('Compressive Strength Concrete Predictor')
    # st.image("""https://civildigital.com/wp-content/uploads/2016/07/Hydraulic-Compression-Testing-Machine.jpg""")
    # st.header('Enter the Components of Concrete') 


    # if st.button('Componets of Concrete'):
    #     compressive_strength = predict(cement, blast_furnace_slag, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age )
    #     st.success(f'The predicted compressive strength of concrete is ${compressive_strength:.2f}')

    if st.button("Predict"):
        result=predict(cement, blast_furnace_slag, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Made with Love & Streamlit")
        st.text("by RAM JAS MAURYA")
        st.text("for ineoron.ai project")



if __name__ == "__main__":
    main()
    


# #@app.route('/predict',methods=["Get"])
# def predict_note_authentication(variance,skewness,curtosis,entropy):
    
#     """Let's Authenticate the Banks Note 
#     This is using docstrings for specifications.
#     ---
#     parameters:  
#       - name: variance
#         in: query
#         type: number
#         required: true
#       - name: skewness
#         in: query
#         type: number
#         required: true
#       - name: curtosis
#         in: query
#         type: number
#         required: true
#       - name: entropy
#         in: query
#         type: number
#         required: true
#     responses:
#         200:
#             description: The output values
        
#     """
   
#     prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
#     print(prediction)
#     return prediction



# def main():
#     st.title("Bank Authenticator")
#     html_temp = """
#     <div style="background-color:tomato;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
#     </div>
#     """
#     st.markdown(html_temp,unsafe_allow_html=True)
#     variance = st.text_input("Variance","Type Here")
#     skewness = st.text_input("skewness","Type Here")
#     curtosis = st.text_input("curtosis","Type Here")
#     entropy = st.text_input("entropy","Type Here")
#     result=""
#     if st.button("Predict"):
#         result=predict_note_authentication(variance,skewness,curtosis,entropy)
#     st.success('The output is {}'.format(result))
#     if st.button("About"):
#         st.text("Lets LEarn")
#         st.text("Built with Streamlit")

# if __name__=='__main__':
#     main()
    
    
    
