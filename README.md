<h1 align="center"> Automatic Menu Popularity Analysis via Fuzzy Matching-Based Extraction of Customer Reviews </h1>
<h2 align="center"> Makalah IF2211 Strategi Algoritma Semester II Tahun 2024/2025 </h2>

## Deskripsi Program
TasteTrace merupakan program yang melakukan menu popularity analysis otomatis berdasarkan customer reviews yang ada. Pada program ini, kami menerapkan two-tier matching approach dimana program melakukan kombinasi exact matching dan fuzzy matching menggunakan Levenshtein Distance.

## Struktur Project
```
TasteTrace 
├── doc/
│   └── Automatic Menu Popularity Analysis via Fuzzy Matching-Based Extraction of Customer Reviews.pdf
├── src/                        # Folder source code utama
│   ├── database/       
│   │   ├── db_setup.py
│   │   ├── db.sql
│   │   ├── menu.txt
│   │   └── seeder.py
│   ├── model/
│   │   └── fuzzy_match.py
│   └── main.py
├── README.md                  # Dokumentasi utama proyek
└── run.bat                    # Tool untuk compile dan run program
```

## Requirements
<div>
    <table>
      <tr>
        <td>No</td>
        <td>Requirement</td>
        <td>Fungsi</td>
      </tr>
      <tr>
        <td>1</td>
        <td>mysql-connector-python</td>
        <td>Koneksi database MySQLn</td>
      </tr>
      <tr>
        <td>2</td>
        <td>rapidfuzz</td>
        <td>Fuzzy Matching Helper</td>
      </tr>
    </table>
</div>

## Cara Mengkompilasi dan Menjalankan Program
##### Setup Database
1. Masuk ke mysql dengan perintah berikut diikuti dengan input password
   ```
      mysql -u root -p
   ```
2. Tambahkan user dan database baru pada mysql 
    ```
       CREATE USER 'taste_trace'@'localhost' IDENTIFIED BY 'tastetrace';
       CREATE DATABASE taste_trace_db;
       GRANT ALL PRIVILEGES ON cv_db.* TO 'taste_trace'@'localhost';
       FLUSH PRIVILEGES;
   ```
##### Cara Menjalankan Program
1. Clone repository
   ```
    git clone https://github.com/naylzhra/TasteTrace.git
   ```
2. Buka folder repository kemudian jalankan run.bat
   ```
    ./run.bat
   ```

## Author
<div>
    <table>
      <tr>
        <td>NIM</td>
        <td>Nama</td>
      </tr>
      <tr>
        <td>13523079</td>
        <td>Nayla Zahira</td>
      </tr>
    </table>
</div>

<div>
  <strong>Strategi Algoritma IF2211 - Institut Teknologi Bandung</strong><br>
</div>
