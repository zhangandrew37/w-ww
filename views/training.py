import streamlit as st
import pandas as pd
from PIL import Image

def load_view():    
    algo_choice = st.selectbox("Algorithm", ['Random Forest', 'Linear Regression', 'Logistic Regression', 'Decision Tree', 'SVM', 'Naïve Bayes', 'KNN', 'K-means'])
    st.title('Training')
    st.markdown("**Training set**")
    col1, col2 = st.columns(2)
    col1.text("Coefficient of determination ($R^2$)")
    col1.info("0.7565002320512857")
    col2.text("Error (MSE or MAE)")
    col2.info("14.720181896908045")
    st.markdown("**Training set**")
    col1, col2 = st.columns(2)
    col1.text("Coefficient of determination ($R^2$)")
    col1.info("0.7565002320512857")
    col2.text("Error (MSE or MAE)")
    col2.info("14.720181896908045")
    # st.markdown("**Test set**")
    # col1, col2 = st.columns(2)
    # col1.metric("Coefficient of determination ($R^2$)", "0.7565002320512857", "1.2 °F")
    # col2.metric("Error (MSE or MAE)", "14.720181896908045", "-8%")

    #Y_pred_train = rf.predict(X_train)
    #st.info( r2_score(Y_train, Y_pred_train) )
    #st.info( mean_squared_error(Y_train, Y_pred_train) )
    st.write("")
    st.write("")
    st.markdown("**Compare with other algorithms: **")
    st.write("")
    col1, col2 = st.columns(2)
    with col1:
        img = Image.open("assets/images/lazypredict.png")
        st.image(img, width=500)
    with col2:
        img = Image.open("assets/images/lazyplot.png")
        st.image(img, width=800)
    #example_data = open("Data-AI-1.csv")
    #df = pd.read_csv(example_data)
    #st.dataframe(df.style.highlight_max(axis=0))

# temporarily use image while finding fixes for XGBoost on M1 Mac

# def build_model(df):
#     df = df.loc[:100] # FOR TESTING PURPOSE, COMMENT THIS OUT FOR PRODUCTION
#     X = df.iloc[:,:-1] # Using all column except for the last column as X
#     Y = df.iloc[:,-1] # Selecting the last column as Y

#     st.markdown('**1.2. Dataset dimension**')
#     st.write('X')
#     st.info(X.shape)
#     st.write('Y')
#     st.info(Y.shape)

#     st.markdown('**1.3. Variable details**:')
#     st.write('X variable (first 20 are shown)')
#     st.info(list(X.columns[:20]))
#     st.write('Y variable')
#     st.info(Y.name)

#     # Build lazy model
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size = split_size,random_state = seed_number)
#     reg = LazyRegressor(verbose=0,ignore_warnings=False, custom_metric=None)
#     models_train,predictions_train = reg.fit(X_train, X_train, Y_train, Y_train)
#     models_test,predictions_test = reg.fit(X_train, X_test, Y_train, Y_test)

#     st.subheader('2. Table of Model Performance')

#     st.write('Training set')
#     st.write(predictions_train)

#     st.write('Test set')
#     st.write(predictions_test)

#     st.subheader('3. Plot of Model Performance (Test set)')


#     with st.markdown('**R-squared**'):
#         # Tall
#         predictions_test["R-Squared"] = [0 if i < 0 else i for i in predictions_test["R-Squared"] ]
#         plt.figure(figsize=(3, 9))
#         sns.set_theme(style="whitegrid")
#         ax1 = sns.barplot(y=predictions_test.index, x="R-Squared", data=predictions_test)
#         ax1.set(xlim=(0, 1))
#         # Wide
#     plt.figure(figsize=(9, 3))
#     sns.set_theme(style="whitegrid")
#     ax1 = sns.barplot(x=predictions_test.index, y="R-Squared", data=predictions_test)
#     ax1.set(ylim=(0, 1))
#     plt.xticks(rotation=90)
#     st.pyplot(plt)

#     with st.markdown('**RMSE (capped at 50)**'):
#         # Tall
#         predictions_test["RMSE"] = [50 if i > 50 else i for i in predictions_test["RMSE"] ]
#         plt.figure(figsize=(3, 9))
#         sns.set_theme(style="whitegrid")
#         ax2 = sns.barplot(y=predictions_test.index, x="RMSE", data=predictions_test)
#         # Wide
#     plt.figure(figsize=(9, 3))
#     sns.set_theme(style="whitegrid")
#     ax2 = sns.barplot(x=predictions_test.index, y="RMSE", data=predictions_test)
#     plt.xticks(rotation=90)
#     st.pyplot(plt)

#     with st.markdown('**Calculation time**'):
#         # Tall
#         predictions_test["Time Taken"] = [0 if i < 0 else i for i in predictions_test["Time Taken"] ]
#         plt.figure(figsize=(3, 9))
#         sns.set_theme(style="whitegrid")
#         ax3 = sns.barplot(y=predictions_test.index, x="Time Taken", data=predictions_test)
#         # Wide
#     plt.figure(figsize=(9, 3))
#     sns.set_theme(style="whitegrid")
#     ax3 = sns.barplot(x=predictions_test.index, y="Time Taken", data=predictions_test)
#     plt.xticks(rotation=90)
#     st.pyplot(plt)
