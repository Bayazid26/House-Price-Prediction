from sklearn.linear_model import LinearRegression
import joblib

model = LinearRegression()

# assume X_train, y_train already exist
model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")