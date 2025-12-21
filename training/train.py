import mlflow
import pandas as pd
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
 
mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("california-housing")

df=pd.read_csv("data/raw_data.csv")
df.rename(columns={"median_house_value":"MedHouseVal"},inplace=True)
df.drop(columns=["ocean_proximity"],inplace=True)
 
X = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]
 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
 
with mlflow.start_run():
    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=10,
        random_state=42
    )
 
    model.fit(X_train, y_train)
 
    preds = model.predict(X_test)
 
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
 
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)
 
    mlflow.sklearn.log_model(
        model,
        artifact_path="sk_model",
        registered_model_name="California_Housing_Model"
    )
