# 🎓 Student Performance Prediction (Machine Learning + FastAPI)

## 📌 Project Overview

This project predicts **student exam scores** based on several factors such as study hours, attendance, motivation level, internet access, parental involvement, and more.

The model is built using **Machine Learning (Scikit-Learn)** and deployed as a **REST API using FastAPI**.
The API allows users to send student attributes and receive a predicted exam score.

---

# 📊 Dataset

Dataset: **Student Performance Factors**

Features used include:

* Hours Studied
* Attendance
* Sleep Hours
* Previous Scores
* Tutoring Sessions
* Physical Activity
* Parental Involvement
* Access to Resources
* Extracurricular Activities
* Motivation Level
* Internet Access
* Family Income
* Parental Education Level
* Distance from Home
* Gender

Target Variable:

**Exam Score**

Dataset size:

```
Rows: 6607
Columns: 20
```

---

# ⚙️ Machine Learning Workflow

### 1️⃣ Data Preprocessing

* Missing value handling
* Categorical encoding using **pd.get_dummies()**
* Feature cleaning
* Train-test split

### 2️⃣ Model Training

Several regression algorithms were trained and evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

### 3️⃣ Model Evaluation

Models were evaluated using:

* R² Score
* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Cross Validation

---

# 📈 Model Performance

| Model             | R² Score   |
| ----------------- | ---------- |
| Linear Regression | **0.7696** |
| Gradient Boosting | 0.7303     |
| Random Forest     | 0.6471     |
| Decision Tree     | 0.5537     |

**Final Model Selected:**
Linear Regression (Best performance)

Cross Validation Score:

```
Average R² ≈ 0.726
```

---

# 🚀 FastAPI Model Deployment

The trained model is deployed using **FastAPI**.

### API Endpoint

```
POST /predict
```

### Example Input

```json
{
 "hours_studied": 4,
 "attendance": 85,
 "sleep_hours": 7,
 "previous_scores": 70,
 "tutoring_sessions": 1,
 "physical_activity": 3,
 "parental_involvement_Low": 0,
 "parental_involvement_Medium": 1,
 "access_to_resources_Low": 0,
 "access_to_resources_Medium": 1,
 "extracurricular_activities_yes": 1,
 "motivation_level_low": 0,
 "motivation_level_medium": 1,
 "internet_access_yes": 1,
 "family_income_low": 0,
 "family_income_medium": 1,
 "parental_education_level_high_school": 1,
 "parental_education_level_postgraduate": 0,
 "distance_from_home_moderate": 1,
 "distance_from_home_near": 0,
 "gender_male": 1
}
```

### Example Output

```json
{
 "predicted_exam_score": 72.4
}
```

---

# 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-Learn
* FastAPI
* Uvicorn
* Pickle

---

# 📁 Project Structure

```
student-performance-prediction
│
├── std_per_factor.ipynb
├── encoded_student_data.csv
├── student_score_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

# ▶️ Running the Project Locally

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/student-performance-prediction.git
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the API

```
uvicorn app:app --reload
```

### 4️⃣ Open API docs

```
http://127.0.0.1:8000/docs
```

---

# ☁️ Deployment

The project is deployed using **Render**.

Deployment Steps:

1. Push the project to GitHub
2. Connect GitHub repository to Render
3. Set start command:

```
uvicorn app:app --host 0.0.0.0 --port 10000
```

---

# 📌 Future Improvements

* Add Streamlit UI
* Hyperparameter tuning
* Feature importance visualization
* Docker containerization

---

# 👨‍💻 Author

**Ashish Jadhav**

 Data Science
