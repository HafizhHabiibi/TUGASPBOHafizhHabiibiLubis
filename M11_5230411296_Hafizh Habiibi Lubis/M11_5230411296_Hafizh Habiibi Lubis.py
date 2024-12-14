# import library
import pandas as pd
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# definisi missing value dan baca dataset
missing_values = ["NaN", "."]
data = pd.read_excel("air_quality.xlsx")
# print(data)

# cek missing value
# print(data.isnull().sum())

# isi missing value
data ['Temperature'] = data ['Temperature'].fillna(data['Temperature'].median())
data ['Humidity'] = data ['Humidity'].fillna(data['Humidity'].median())
data ['PM2.5'] = data ['PM2.5'].fillna(data['PM2.5'].median())
data ['PM10'] = data ['PM10'].fillna(data['PM10'].median())
data ['NO2'] = data ['NO2'].fillna(data['NO2'].median())
data ['SO2'] = data ['SO2'].fillna(data['SO2'].median())
data ['CO'] = data ['CO'].fillna(data['CO'].median())
data ['Proximity_to_Industrial_Areas'] = data ['Proximity_to_Industrial_Areas'].fillna(data['Proximity_to_Industrial_Areas'].median())
data ['Population_Density'] = data ['Population_Density'].fillna(data['Population_Density'].median())

# isi missing value untuk objek
data ['Air Quality'] = data['Air Quality'].fillna(data['Air Quality'].mode()[0])

# print(data)

# cek ulang missing value
# print(data.isnull().sum())

# label encoder
column = ['Air Quality']
encoder = LabelEncoder()

for i in column:
    data[i] = encoder.fit_transform(data[i])

# print(data)

# definisi feature dan label 

feature = data.drop('Air Quality', axis=1).values  # Semua kolom kecuali target
label = data['Air Quality'].values # Kolom targets

scaler = MinMaxScaler()
feature = scaler.fit_transform(feature)

# spliting data train dan data test
x_train, x_test, y_train, y_test = train_test_split(feature, label, test_size=0.2, random_state=42)
# print(f"Data Train : {len(x_train)}")
# print(f"Data Test : {len(x_test)}")


while True:
    try:
        print("="*30 + "PILIH ALGORITMA" + "="*30)
        print("1. Naive Bayes")
        print("2. Decision Tree")
        print("3. Tampilkan Semua Data")
        print("4. Keluar")

        pilih = int(input("Masukan Pilihan : "))

        if pilih == 1:

            model = GaussianNB()

            model.fit(x_train, y_train)
            pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, pred)
            print(f"Akurasi Model : {accuracy}")

            os.system("pause")
            
        if pilih == 2:
            model = DecisionTreeClassifier()

            model.fit(x_train, y_train)
            pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, pred)
            print(f"Akurasi Model : {accuracy}")

            os.system("pause")

        if pilih == 3:
            print(data)

            os.system("pause")

        if pilih == 4:
            break

        os.system("cls")

    except ValueError:
        print("INPUTAN HARUS ANGKA!")