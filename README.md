# Python-API

# Aplikasi CRUD FastAPI dengan MySQL

Aplikasi sederhana menggunakan FastAPI dengan backend MySQL untuk operasi CRUD dasar. Proyek ini mencakup:

- **Server**: Aplikasi FastAPI (`server.py`) dengan endpoint untuk Create, Read, Update, dan Delete.
- **Client**: Python client (`client.py`) dengan antarmuka menu untuk berinteraksi dengan API.
- **Database**: Integrasi database MySQL untuk menyimpan dan mengelola data.
- **Dokumentasi API**: Swagger UI interaktif yang disediakan oleh FastAPI.

---

## Fitur

- API RESTful untuk operasi CRUD.
- Dokumentasi Swagger untuk pengujian API yang mudah.
- Python client untuk berinteraksi dengan API langsung dari terminal.

---

## Instalasi dan Setup

### 1. Clone Repositori
Repository bisa di clone via URL atau download ZIP file. Disarankan untuk download ZIP File saja.
```bash
git clone https://github.com/<username-anda>/<nama-repositori-anda>.git
cd <nama-repositori-anda>


```

---

### 2. **Membuat dan Aktivasi Virtual Environment**
Salin kode ke windows CMD.

```bash

python -m venv pyapi

pyapi\Scripts\activate

pip install -r requirements.txt
```

---

### 3. **Konfigurasi Database MySQL**
Buat database MySQL:
```bash
CREATE DATABASE test_db;
USE test_db;
CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL
);
```

---

### 4. **Menjalankan Aplikasi**
## 1.  *Jalankan Server*
```bash
py server.py

```
API dapat diakses di http://127.0.0.1:8000. Dokumentasi Swagger tersedia di http://127.0.0.1:8000/docs.

---


## 2. *Uji API*
Jalankan client untuk berinteraksi dengan API:
```bash
python client.py

```
Gunakan menu untuk melakukan operasi CRUD:

- Create Item: Tambahkan data baru.
- Read All Items: Tampilkan semua data.
- Read Item by ID: Tampilkan data berdasarkan ID.
- Update Item: Perbarui data berdasarkan ID.
- Delete Item: Hapus data berdasarkan ID

---