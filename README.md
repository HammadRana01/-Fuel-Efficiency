# Fuel Efficiency Prediction using TensorFlow

## 📌 Project Overview
This project implements a deep learning model to predict the fuel efficiency (MPG) of vehicles based on various features such as horsepower, cylinders, and origin. The model is built using **TensorFlow** and **Keras**, with data preprocessing, exploratory data analysis, and model evaluation included.

## 📂 Dataset
The dataset used is the **Auto MPG dataset**, which contains vehicle specifications and fuel efficiency values.

### **Features:**
- `mpg` (Miles per gallon - Target Variable)
- `cylinders`
- `displacement`
- `horsepower`
- `weight`
- `acceleration`
- `model year`
- `origin`
- `car name` (Removed during preprocessing)

## 🛠️ Technologies Used
- **Python**
- **TensorFlow & Keras**
- **Pandas & NumPy**
- **Matplotlib & Seaborn**
- **Scikit-Learn**

## 🚀 Project Structure
```
📦 Fuel-Efficiency-Prediction
├── 📂 dataset
│   ├── auto-mpg.csv
├── 📂 notebooks
│   ├── data_preprocessing.ipynb
│   ├── model_training.ipynb
├── src
│   ├── train_model.py
│   ├── evaluate_model.py
├── README.md
├── requirements.txt
└── model.h5
```

## 🔧 Installation & Setup
1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/Fuel-Efficiency-Prediction.git
   cd Fuel-Efficiency-Prediction
   ```

2. **Create a virtual environment (Optional but recommended)**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the training script**
   ```sh
   python src/train_model.py
   ```

5. **Evaluate the model**
   ```sh
   python src/evaluate_model.py
   ```

## 📊 Results & Visualizations
- **Heatmaps** to show feature correlations.
- **Bar charts** for categorical feature analysis.
- **Loss & MAPE plots** for training and validation performance.

## 📌 Future Improvements
- **Hyperparameter tuning** for better performance.
- **Incorporating additional vehicle attributes**.
- **Deploying the model using Flask or FastAPI**.

## 📜 License
This project is licensed under the MIT License.

---
### 👨‍💻 Developed by **Hammad Rana**

