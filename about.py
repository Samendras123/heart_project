import streamlit as st

def main():
    st.header("How the Project is Working?")

    st.image("./img2.gif")

    st.subheader("Machine Learning Steps")
    st.write("**1. Gather and Preprocess Data:** Collect relevant data for your machine learning task. This data may include structured data from databases, unstructured data from text documents or images, or other types of data. Preprocess the data by cleaning, transforming, and normalizing it to ensure it is in a suitable format for analysis.")
    st.write("**2. Split the Data:** Divide the dataset into two or more subsets: **a training set and a testing set**. The training set is used to train the machine learning model, while the testing set is used to evaluate the model's performance on unseen data.")
    st.write("**3. Select a Model:** Choose an appropriate machine learning model or algorithm that is suitable for your problem. The choice of model depends on the nature of the data, the problem you are solving (classification, regression, clustering, etc.), and other factors. We use hera **Random Forest Algorithm** which is an ensemble method.")
    st.write("**4. Train the Model:** Use the training set to train the chosen model. During training, the model learns patterns and relationships in the data to make predictions or classifications. This involves adjusting the model's internal parameters using **optimization algorithms to minimize errors or maximize performance.**")
    st.write("**5. Evaluate the Model:** Assess the performance of the trained model using the test/validation set. Common evaluation metrics include **accuracy, precision, recall, F1-score, mean squared error,** and others, depending on the problem type. This step helps to understand how well the model generalizes to unseen data and whether it meets the desired performance criteria.")
    st.write("**6. Tune Hyperparameters:** Adjust the hyperparameters of the model to optimize its performance. Hyperparameters are settings that control the learning process and can impact the model's performance. Techniques like **cross-validation or grid search** can be used to find the optimal values for these hyperparameters.")
    st.write("**7. Deploy the Model:** Once you are satisfied with the model's performance, deploy it in a production environment to make predictions or classifications on new, unseen data. This may involve integrating the model into an application, setting up APIs, or creating a pipeline for real-time inference.")
