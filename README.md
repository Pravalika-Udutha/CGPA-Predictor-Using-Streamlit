# CGPA Predictor Using Streamlit

Welcome to the **CGPA Predictor Using Streamlit** project! This is a simple web application built with Python, Streamlit, and Scikit-Learn to predict a student's placement package (in LPA) based on their CGPA. The app uses a Simple Linear Regression model trained on a sample dataset and provides an interactive interface for users to input their CGPA and get predictions.

## Features
- **User-Friendly Interface**: Enter your CGPA through a simple input field in the Streamlit app.
- **Real-Time Prediction**: Get instant predictions of your placement package based on the trained model.
- **Simple Linear Regression**: Uses Scikit-Learn's LinearRegression model for accurate predictions.

## Project Structure
``` Pattern
CGPA-Predictor-Using-Streamlit/
│
├── app.py              # Main Streamlit application file
├── placement.csv       # Sample dataset (CGPA and Package)
├── requirements.txt    # List of required Python libraries
└── README.md           # Project documentation (this file)
```


## Installation
Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pravalika-Udutha/CGPA-Predictor-Using-Streamlit.git
   cd CGPA-Predictor-Using-Streamlit
   ```
2. **Install Dependencies**:

Ensure you have Python installed (version 3.7+ recommended). Then install the required libraries:

```bash
pip install -r requirements.txt
```
3. **Launch the App**:
```bash
streamlit run app.py
```
Open your browser and go to http://localhost:8501 to see the app in action.
``

## How It Works

- **Data Loading**: The app loads the `placement.csv` dataset using Pandas.  
- **Model Training**: A Simple Linear Regression model is trained using Scikit-Learn on the CGPA and package data.  
- **Prediction**: The user inputs a CGPA value, which is reshaped to a 2D array and passed to the model for prediction.  
- **Output**: The predicted package is displayed on the Streamlit interface.  

## Usage

1. Open the app in your browser.  
2. Enter your CGPA (e.g., `7.5`) in the sidebar input field.  
3. Click the **"Find Package"** button.  
4. See the predicted package value displayed on the screen (e.g., **"Predicted Package: 3.45 LPA"**).

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Any contributions are welcome!

1. Fork the repo.
2. Create a new branch (git checkout -b feature-branch).
3. Commit your changes (git commit -m "Add new feature").
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.


## Author

 Pravalika Udutha.
 
 GitHub: [Pravalika Udutha](https://github.com/Pravalika-Udutha).





