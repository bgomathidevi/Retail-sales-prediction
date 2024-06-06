# Retail-sales-prediction

Project Overview:
    This project aims to forecast department-wise weekly sales for each store for the following year using historical sales data.       
    Accurate sales predictions help make informed business decisions, especially during holiday periods and promotional markdown events.

Business Use Cases:
1. Sales Forecasting: Predict future sales to manage inventory effectively and reduce stockouts or overstock situations.
2. Promotional Planning: Understand the effectiveness of markdowns and plan future promotional activities.
3. Resource Allocation: Allocate resources such as staffing and marketing budget based on predicted sales peaks.
4. Holiday Strategy: Optimize holiday-specific strategies to maximize revenue during peak seasons.
   
Skills and Technologies:
   Skills: Machine Learning/Deep Learning Deployment, Time Series Analysis, Predictive Modeling, Data Preprocessing, Feature Engineering, 
Exploratory Data Analysis (EDA), Model Evaluation and Validation, Impact Analysis of Promotions and Holidays, Data Visualization.
   Technologies: Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Streamlit, Scikit-learn.
   
Approach:

Data Understanding and Preprocessing:

1. Handle missing values and convert date formats.
2. Extract features like year, month, and week number.
3. Normalize or scale numerical data.

Exploratory Data Analysis (EDA):

1. Visualize trends, seasonality, and the impact of holidays.
2. Analyze correlations between sales and other features.

Feature Engineering:

1. Create new features such as lagged sales, rolling averages, and holiday flags.
2. Encode categorical variables as needed.

Model Selection and Training:

1. Split data into training and validation sets.
2. Train various models (e.g., ARIMA, Random Forest, LSTM).
3. Evaluate models using metrics like RMSE and MAE, with a focus on holiday weeks.

Markdown Effect Analysis:

1. Simulate sales with and without markdowns.
2. Quantify the impact of markdowns on sales.

Recommendations:

1. Provide actionable insights for markdown strategies and holiday planning.
2. Suggest improvements for future data collection.

Results:
1. Sales Forecasts: Accurate weekly sales predictions for each department.
2. Markdown Insights: Quantitative analysis of markdown impacts on sales.
3. Strategic Recommendations: Data-driven suggestions for promotional and holiday strategies to maximize business impact.
   
Project Evaluation Metrics:
1. Root Mean Squared Error (RMSE)
2. Mean Absolute Error (MAE)
3. Weighted Metrics: Higher weights for holiday weeks to reflect their importance.

Home: Overview of the project, domain, and technologies used.

Prediction: Input the details of the store, department, markdowns, and other features to get weekly sales predictions.

Conclusion: Summary of model performance and final observations.

Model Performance:
1. Linear Regressor Accuracy: 84.88%
2. Random Forest Regressor Accuracy: 95.45%
3. Decision Tree Regressor Accuracy: 94.08%
4. K Neighbors Regressor Accuracy: 91.97%
5. XGBoost Accuracy: 94.21%
6. DNN Accuracy: 90.50%
The Random Forest Regressor was chosen as the final model due to its highest accuracy of 95.45%.

Final Observations:
1. Larger stores tend to have higher sales.
2. Fuel Price and Unemployment rate significantly impact weekly sales.
3. Temperature and Markdowns are crucial during key promotional events.
4. Proper planning and execution of markdown strategies can drive substantial sales increases during holidays.

License:
 MIT
