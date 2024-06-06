import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import datetime 
import pickle
from streamlit_option_menu import option_menu
from datetime import datetime as dt
from sklearn import metrics
import seaborn as sns
from scipy import stats

from sklearn.ensemble import RandomForestRegressor

#====================================================================================================
df=pd.read_csv(r'G:\PROJECT\Final project\final_data.csv')
df=df.drop(['Unnamed: 0'],axis=1)


#------------------------------------------------------------------------------------------------------------------------------------------

#page congiguration
page_bg_img='''
<style>
[data-testid="stAppViewContainer"]{
        background-color: #D3D3D3;  
}
</style>'''
st.set_page_config(page_title= "Retail_Sales_Prediction | By Gomathidevi",
                layout= "wide",
                initial_sidebar_state= "expanded",)
st.markdown("<h1 style='text-align: center; color: violet;'>Retail Weekly Sales Predicton</h1>", unsafe_allow_html=True)
st.markdown(page_bg_img,unsafe_allow_html=True)

#===============================================================================================================================================
with st.sidebar:
    selected = option_menu(
        "Menu",
        [ "HOME", "PREDICTION", "CONCLUSION"],
        icons=[ "house", "graph-up", "check-circle"],
        menu_icon="menu-button-wide",
        default_index=0,
        styles={"nav-link": {"font-size": "17px", "text-align": "left", "margin": "-2px", "--hover-color": "#000000"},
                "nav-link-selected": {"background-color": "#000000"}}
    )


if selected == "HOME":
    col1,col2=st.columns(2,gap="large")

    with col1:
        col1.markdown("#### :red[Domain]")
        st.write("##### Retail Industry")
        st.write()
        col1.markdown("#### :red[Technologies  and Tools used]")
        st.write("##### Python, Pandas, numpy, matplotlib, seaborn, Plotly, Streamlit, sklearn.")
        st.write()
        col1.markdown("#### :red[Overview of the Project] ")
        st.write("##### *  Predict the weekly sales of a retail store based on historical sales using Machine Learning techniques. ")
        st.write("##### *  To perform Data cleaning, Exploratory Data Analysis, Feature Engineering, Hypothesis Testing for the ML model. ")
        st.write("##### *  In this use case I used the :violet[RANDOM FOREST REGRESSOR] model to predict the weekly sales of the retail store. ")

    with col2:
        col2.image(Image.open(r"G:\PROJECT\Final project\2.jpg"), width=700)   

  


if selected == "PREDICTION":
    option = st.radio('**Select your option**',('Processed Data', 'Prediction Process',),horizontal=True)

    if option == 'Processed Data':
        st.header("Processed  Final Data")
        st.write(df)

    if option == 'Prediction Process':

        col3,col4,col5,col6,col10=st.columns(5,gap="large")

        with col3:

            st.header(":violet[Store info]")

            # store
            store_no = [i for i in range(1, 46)] 

            store = st.selectbox('Select the **:red[Store Number]**', store_no)

            # department
            dept_no = [ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 
                        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,33, 34, 35, 36, 37, 38, 40, 
                        41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55,56, 58, 59, 60, 67, 71, 72, 
                        74, 79, 80, 81, 82, 83, 85, 87, 90, 91, 92, 93, 94, 95, 97, 78, 96, 99, 39,
                        77, 50, 43, 65, 98]

            dept = st.selectbox('Select the **:red[Department Number]**', dept_no)

            # Type
            Type = {'A':0,"B":1,"C":2}

            type_ = st.selectbox('Select the **:red[Store Type]**', ['A', 'B', 'C'])

            # Size
            size=[151315, 202307,  37392, 205863,  34875, 202505,  70713, 155078,
                  125833, 126512, 207499, 112238, 219622, 200898, 123737,  57197,
                  93188, 120653, 203819, 203742, 140167, 119557, 114533, 128107,
                  152513, 204184, 206302,  93638,  42988, 203750, 203007,  39690,
                  158114, 103681,  39910, 184109, 155083, 196321,  41062, 118221]
            
            siz=st.selectbox('Select the **:red[Store Size]**', size)



        with col4:

            st.header(":violet[Indirect Impact on Store Sales]")

            # TEMPERATURE
            temp = st.number_input('Enter the ****:red[Temperature]**** in fahrenheit -----> **:green[(min=5.54 & max=100.14)]**',value=90.0,min_value=5.54,max_value=100.14)
            
            # Fuel Price
            fuel = st.number_input('Enter the **:red[Fuel Price]** ---> **:green[(min=2.472 & max=4.468)]**',value=3.67,min_value=2.472,max_value=4.468)

            # Consumer Price Index
            CPI = st.number_input('Enter the **:red[CPI]** ----------> **:green[(min=126.0 & max=227.47)]**',value=211.77,min_value=126.0,max_value=227.47)

                # min : 126.064
                # max : 227.2328068
            # Unemployment
            unemp = st.number_input('Enter the **:red[Unemployment Rate]** in percentage **:green[(min=3.879 & max=14.313)]**',value=8.106,min_value=3.879,max_value=14.313)

            # min : 3.879
            # max : 14.313    


        with col5: 
            st.header(":violet[Markdown are Impact on Store Sales]")   

            # markown
            def inv_trans(x):
                return 1/x

            markdown1 = st.number_input('Enter the **:red[Markdown1]** in dollars -------- **:green[(min=0.27,max=88646.76)]**',value=2000.00,min_value=0.27,max_value=88646.76)
            markdown1=inv_trans(markdown1)

            markdown2 = st.number_input('Enter the **:red[Markdown2]** in dollars -------- **:green[(min=0.02,max=104519.54)]**',value=65000.00,min_value=0.02,max_value=104519.54)
            markdown2=inv_trans(markdown2)

            markdown3=st.number_input('Enter the **:red[Markdown3]** in dollars -------- **:green[(min=0.01,max=141630.61)]**',value=27000.00,min_value=0.01,max_value=141630.61)
            markdown3=inv_trans(markdown3)

            markdown4=st.number_input('Enter the **:red[Markdown4]** in dollars -------- **:green[(min=0.22,max=67474.85))]**',value=11200.00,min_value=0.22,max_value=67474.85)
            markdown4=inv_trans(markdown4)

            markdown5=st.number_input('Enter the **:red[Markdown5]** in dollars -------- **:green[(min=135.06,max=108519.28)]**',value=89000.00,min_value=135.06,max_value=108519.28)
            markdown5=inv_trans(markdown5)



        with col6:
            st.header(":violet[Direct Impact on Store Sales]")
            
            # Date
            duration = st.date_input("Select the **:red[Date]**", datetime.date(2012, 7, 20), min_value=datetime.date(2010, 2, 5), max_value=datetime.date.today())

            # Holiday
            holi={"YES":1,"NO":0}

            holiday = st.selectbox('Select the **:red[Holiday]**', ["YES","NO"])     
            




        with col10:
            st.header(":red[Weekly Sales]")  

            import pickle
            model=pickle.load(open(r'G:\PROJECT\Final project\model.pkl', 'rb'))

            if st.button('Predict'):

                result = model.predict([[store,dept,siz,temp, fuel,CPI, unemp, markdown1,markdown2,markdown3,markdown4,markdown5, duration.year,duration.month,duration.day,Type[type_] ,holi[holiday]]])
                
                #predicted_price = str(result)[1:-1]
                price=result.round(2)

                st.warning(f'Predicted weekly sales of the retail store is: $ {price}')


if selected == "CONCLUSION":

    col8,col9=st.columns(2,gap="large")
    with col8:

        st.subheader(":violet[Model Performance]")
        st.write("""
        The accuracy of various machine learning models was evaluated:
        - Linear Regressor Accuracy: **:red[84.88%]**
        - Random Forest Regressor Accuracy: **:red[95.45%]**
        - Decision Tree Regressor Accuracy: **:red[94.08%]**
        - K Neighbors Regressor Accuracy: **:red[91.97%]**
        - XGBoost Accuracy: **:red[94.21%]**
        - DNN Accuracy: **:red[90.50%]**

        Based on the accuracy scores, the **:red[Random Forest Regressor]** was chosen as the final model due to its highest accuracy of **:red[95.45%]**.
        """)
        st.write("By leveraging these insights and the **:blue[Random Forest Regressor model]**, the retail store can make data-driven decisions to enhance sales performance and operational efficiency.")
    with col9:
        st.subheader(":violet[Final Observations]")
        st.write("* **:green[Size of the store]**  :Larger stores tend to have higher sales.")
        st.write(" * Combination of **:green[Fuel Price]** and **:green[Unemployment rate]**: These factors significantly impact weekly sales.")
        st.write("* **:green[Temprature]** and **:green[Markdown]** These factors can have both direct and indirect relationships with sales and are crucial during key promotional events.")
        st.write("*  **:green[Markdowns]**, especially during holidays, play a significant role in boosting sales. Proper planning and execution of markdown strategies before events like the Super Bowl, Christmas, and Thanksgiving can drive substantial sales increases.")
    
    st.image(Image.open(r"G:\PROJECT\Final project\1.jpg"), width=700)    





            
      


    