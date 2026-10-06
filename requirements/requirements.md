# Requirements - HRIS Login

## REQ-LOGIN-001 — Login dengan Credential Valid

User harus dapat login menggunakan username dan password yang valid.

### Test Data
- Username: `zacky`
- Password: `123456`

### Expected Result
Sistem menampilkan pesan:

`Login berhasil`

---

## REQ-LOGIN-002 — Validasi Password Salah

Sistem harus menolak login apabila user memasukkan password yang salah.

### Test Data
- Username: `zacky`
- Password: `salah123`

### Expected Result
Sistem menampilkan pesan:

`Username atau password salah`

---

## REQ-LOGIN-003 — Validasi Username Kosong

Sistem harus memberikan validasi apabila username tidak diisi.

### Test Data
- Username: kosong
- Password: `123456`

### Expected Result
Sistem menampilkan pesan:

`Username wajib diisi`

---

## REQ-LOGIN-004 — Validasi Password Kosong

Sistem harus menolak login apabila password tidak diisi.

### Test Data
- Username: `zacky`
- Password: kosong

### Expected Result
Sistem menampilkan pesan:

`Username atau password salah`

---

## REQ-LOGIN-005 — Validasi Username dan Password Kosong

Sistem harus memberikan validasi apabila username dan password tidak diisi.

### Test Data
- Username: kosong
- Password: kosong

### Expected Result
Sistem menampilkan pesan:

`Username wajib diisi`