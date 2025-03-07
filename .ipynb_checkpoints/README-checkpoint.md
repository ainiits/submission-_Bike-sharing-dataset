{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "017193ad-91e1-4aeb-b705-e33ea22dd042",
   "metadata": {},
   "source": [
    "# **Bike-Sharing Dataset Dashboard 🚴**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f9584ad9-10c7-4365-81ed-6d7ffc40e393",
   "metadata": {},
   "source": [
    "## **Deskripsi**:\n",
    "\n",
    "Dashboard interaktif yang dibuat menggunakan Streamlit untuk menganalisis data penyewaan sepeda berdasarkan berbagai faktor seperti musim, kondisi cuaca, jam, dan hari kerja vs hari libur. Dashboard ini memungkinkan pengguna untuk menyaring data sesuai dengan rentang waktu dan kategori yang diinginkan."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a454872e-825d-48c7-b76b-afa8ee713dfe",
   "metadata": {},
   "source": [
    "## **Setup Environment**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0b05f23-cdc6-4800-99ab-95743857c60a",
   "metadata": {},
   "outputs": [],
   "source": [
    "mkdir submission\n",
    "cd submission\n",
    "pipenv install\n",
    "pipenv shell\n",
    "pip install -r requirements.txt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8ae40ccf-6efb-4ba2-abd3-781463499b3d",
   "metadata": {},
   "source": [
    "## **Run streamlit app**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df018f72-ffc2-48ea-a462-ad5454eebc0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "streamlit run dashboard.py"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
