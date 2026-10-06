# Bug Report - HRIS Login

## BUG-001 - User dapat login menggunakan password yang salah atau kosong

### Module
Login

### Severity
Critical

### Priority
High

### Environment
- OS: Windows
- Browser: Google Chrome
- Python: 3.14.0
- Selenium: 4.50.0
- PyTest: 9.1.1

### Description
Sistem dapat menampilkan pesan "Login berhasil" ketika username yang digunakan adalah `zacky`, meskipun password yang dimasukkan salah atau kosong.

### Steps to Reproduce

1. Buka halaman Login HRIS.
2. Masukkan username `zacky`.
3. Masukkan password yang salah, misalnya `salah123`.
4. Klik tombol "Masuk".
5. Perhatikan pesan yang ditampilkan.

### Test Data

**Username:** `zacky`  
**Password:** `salah123`

### Expected Result

Sistem menolak login dan menampilkan:

`Username atau password salah`

### Actual Result

Sistem menampilkan:

`Login berhasil`

### Additional Finding

Bug yang sama ditemukan ketika username `zacky` digunakan tanpa memasukkan password.

### Automation Test Result

- TC-002: FAILED
- TC-004: FAILED
- 3 test case lainnya: PASSED

**Total: 2 Failed, 3 Passed**

### Root Cause

Validasi pada kode login hanya memeriksa username `zacky` dan tidak memvalidasi password dengan benar.

### Status

Fixed - Menunggu Retesting