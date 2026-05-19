import pandas as pd
import numpy as np


df = pd.read_csv(r'C:\Users\belzs\Documents\DATA ANALYST\Data House\train.csv')

correlation = df.select_dtypes(include=['number']).corr()['SalePrice'].sort_values(ascending=False)
feature = ['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt', 'SalePrice' ]
df_new = df[feature].copy()
df_new.isna().sum()
df_new.to_csv('train_new.csv', index = False)
df = pd.read_csv(r'C:\Users\belzs\Documents\DATA ANALYST\Bike Store\venvv\train_new.csv')
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pickle

X = df[['OverallQual', 'GrLivArea', 'GarageCars', 'GarageArea', 'TotalBsmtSF', '1stFlrSF', 'FullBath', 'TotRmsAbvGrd', 'YearBuilt']]
y = df['SalePrice']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2 , random_state=42)
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test,y_pred))

print("Hasil Evaluasi Model")
print(f"R2 Score (Kebaikan Model): {r2:.4f}")
print(f"Rata rata error meleset: {rmse: .2f}")

with open('model_rumah_kaggle.pkl', 'wb') as f:
    pickle.dump(model, f)

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title= 'API Prediksi Harga Rumah Kaggle')

with open('model_rumah_kaggle.pkl', 'rb') as f:
    model_loaded = pickle.load(f)

class SpesifikasiRumah(BaseModel):
    OverallQual: int
    GrLivArea : int
    GarageCars : int
    GarageArea : int
    TotalBsmtSF : int
    first_flr_sf: int = Field(..., alias="1stFlrSF")
    FullBath : int
    TotRmsAbvGrd : int
    YearBuilt : int

@app.post("/predict_price")
def prediksi_harga(data: SpesifikasiRumah):
    input_data = np.array([[data.OverallQual, data.GrLivArea, data.GarageCars, data.GarageArea, data.TotalBsmtSF, data.first_flr_sf ,data.FullBath, data.TotRmsAbvGrd, data.YearBuilt]])
    harga_prediksi = model_loaded.predict(input_data)[0]
    return {
        "status": "Sukses",
        "perkiraan_harga_jual": f"${round(harga_prediksi, 2)}",
        "detail_properti": {
            "kualitas_bahan_dan_selesai_kondisi (1-10)": data.OverallQual,
            "luas_ruang_tamu_atas_tanah": f"{data.GrLivArea} sqft",
            "kapasitas_mobil_garasi": f"{data.GarageCars} mobil",
            "luas_area_garasi": f"{data.GarageArea} sqft",
            "luas_area_bawah_tanah_basement": f"{data.TotalBsmtSF} sqft",
            "luas_lantai_pertama": f"{data.first_flr_sf} sqft",
            "jumlah_kamar_mandi_lengkap": data.FullBath,
            "total_kamar_di_atas_tanah_excl_toilet": data.TotRmsAbvGrd,
            "tahun_pembangunan_rumah": data.YearBuilt
        }
    }