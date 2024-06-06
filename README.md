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

Handle missing values and convert date formats.
Extract features like year, month, and week number.
Normalize or scale numerical data.

Exploratory Data Analysis (EDA):

Visualize trends, seasonality, and the impact of holidays.
Analyze correlations between sales and other features.
Feature Engineering:

Create new features such as lagged sales, rolling averages, and holiday flags.
Encode categorical variables as needed.

Model Selection and Training:

Split data into training and validation sets.
Train various models (e.g., ARIMA, Random Forest, LSTM).
Evaluate models using metrics like RMSE and MAE, with a focus on holiday weeks.

Markdown Effect Analysis:

Simulate sales with and without markdowns.
Quantify the impact of markdowns on sales.

Recommendations:

Provide actionable insights for markdown strategies and holiday planning.
Suggest improvements for future data collection.

Results:
1. Sales Forecasts: Accurate weekly sales predictions for each department.
2. Markdown Insights: Quantitative analysis of markdown impacts on sales.
3. Strategic Recommendations: Data-driven suggestions for promotional and holiday strategies to maximize business impact.
   
Project Evaluation Metrics:
Root Mean Squared Error (RMSE)
Mean Absolute Error (MAE)
Weighted Metrics: Higher weights for holiday weeks to reflect their importance.

Home: Overview of the project, domain, and technologies used.
Prediction: Input the details of the store, department, markdowns, and other features to get weekly sales predictions.
Conclusion: Summary of model performance and final observations.
Model Performance
Linear Regressor Accuracy: 84.88%
Random Forest Regressor Accuracy: 95.45%
Decision Tree Regressor Accuracy: 94.08%
K Neighbors Regressor Accuracy: 91.97%
XGBoost Accuracy: 94.21%
DNN Accuracy: 90.50%
The Random Forest Regressor was chosen as the final model due to its highest accuracy of 95.45%.

Final Observations:
Larger stores tend to have higher sales.
Fuel Price and Unemployment rate significantly impact weekly sales.
Temperature and Markdowns are crucial during key promotional events.
Proper planning and execution of markdown strategies can drive substantial sales increases during holidays.
Contributing
Feel free to submit issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
MIT
