# Test Scenarios - HRIS Login

## TS-LOGIN-001 — Login dengan Credential Valid

**Requirement:** REQ-LOGIN-001

**Scenario:**  
Memastikan user dapat login menggunakan username dan password yang valid.

**Expected Result:**  
Sistem menampilkan pesan `Login berhasil`.

---

## TS-LOGIN-002 — Login dengan Password Salah

**Requirement:** REQ-LOGIN-002

**Scenario:**  
Memastikan sistem menolak login ketika user memasukkan password yang salah.

**Expected Result:**  
Sistem menampilkan pesan `Username atau password salah`.

---

## TS-LOGIN-003 — Login dengan Username Kosong

**Requirement:** REQ-LOGIN-003

**Scenario:**  
Memastikan sistem memberikan validasi ketika username tidak diisi.

**Expected Result:**  
Sistem menampilkan pesan `Username wajib diisi`.

---

## TS-LOGIN-004 — Login dengan Password Kosong

**Requirement:** REQ-LOGIN-004

**Scenario:**  
Memastikan sistem menolak login ketika password tidak diisi.

**Expected Result:**  
Sistem menampilkan pesan `Username atau password salah`.

---

## TS-LOGIN-005 — Login dengan Username dan Password Kosong

**Requirement:** REQ-LOGIN-005

**Scenario:**  
Memastikan sistem memberikan validasi ketika username dan password tidak diisi.

**Expected Result:**  
Sistem menampilkan pesan `Username wajib diisi`.