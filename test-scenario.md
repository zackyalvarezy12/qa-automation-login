# Test Scenarios - HRIS Login

## TS-001 - Login dengan credential valid

**Scenario:**  
Memastikan user dapat login menggunakan username dan password yang valid.

**Expected:**  
Sistem menampilkan pesan "Login berhasil".

---

## TS-002 - Login dengan password salah

**Scenario:**  
Memastikan sistem menolak login ketika user memasukkan password yang salah.

**Expected:**  
Sistem menampilkan pesan "Username atau password salah".

---

## TS-003 - Login dengan username kosong

**Scenario:**  
Memastikan sistem memberikan validasi ketika username tidak diisi.

**Expected:**  
Sistem menampilkan pesan "Username wajib diisi".

---

## TS-004 - Login dengan password kosong

**Scenario:**  
Memastikan sistem menolak login ketika password tidak diisi.

**Expected:**  
Sistem menampilkan pesan "Username atau password salah".

---

## TS-005 - Login dengan username dan password kosong

**Scenario:**  
Memastikan sistem memberikan validasi ketika username dan password tidak diisi.

**Expected:**  
Sistem menampilkan pesan "Username wajib diisi".