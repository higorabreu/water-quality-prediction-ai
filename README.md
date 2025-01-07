# Water Quality Prediction

This program predicts water quality based on appearance, pH, and turbidity parameters. It uses a fuzzy system to generate data and trains a machine learning model for predictions.

---

## **Project Files**

1. **`sistema_fuzzy.py`**: Defines the fuzzy system used to simulate water quality.  
2. **`banco_de_dados.py`**: Generates input and output data using the fuzzy system.  
3. **`treinamento_modelo.py`**: Trains the model with the generated data.  
4. **`comparacao_saidas.py`**: Compares model predictions with actual data.  
5. **`main.py`**: Centralizes program execution.

---

## **Dependencies**

Install the required libraries using the command:  
```bash
pip install numpy scikit-learn scikit-fuzzy
```

---

## **How to Run**

1. **First Execution**:  
   Run the command below to generate data, train the model, and compare predictions:  
   ```bash
   python main.py
   ```

2. **Regenerate Data and Train the Model**:  
   Use this command to force data generation and retrain the model:  
   ```bash
   python main.py --regenerate
   ```

3. **Compare Outputs Only**:  
   Run this command to skip data generation and use the existing model:  
   ```bash
   python main.py
   ```

---

## **Program Outputs**

- **Score (R²)**: Evaluates model quality (values close to 1 indicate good performance).  
- **Mean Squared Error (MSE)**: Measures prediction accuracy (lower values indicate higher precision).  

---

## **Generated File Structure**

- **`X.npy` and `y.npy`**: Generated input and output data.  
- **`modelo_treinado.pkl`**: Trained model file.  
- **`scaler.pkl`**: Scaler used to normalize data.
