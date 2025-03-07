# Bike-Sharing Dataset Dashboard 🚴
Informasi cara menjalankan dashboard _Bike-Sharing_

## Setup Environment
Ada 2 pilihan untuk membuat virtual environment, yaitu menggunakan conda (jika menginstal Python melalui <ins>Anaconda</ins> ataupun <ins>Miniconda</ins>) dan pipenv (jika menginstal Python melalui <ins>official home</ins>).
Lokasi ada pada folder projek `submission-projek-analisis-data` yang didalamnya terdapat file `requirements.txt`.

### Setup Environment - Anaconda
```
conda create --name main-ds python=3.13
conda activate main-ds
pip install -r requirements.txt
```

### Setup Environment - Shell/Terminal
```
mkdir submission
cd submission
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run streamlit app
```
streamlit run dashboard.py
```
