# Test Execution Report - HRIS Login

## 1. Initial Test Execution

Pengujian awal dilakukan terhadap 5 test case menggunakan Selenium WebDriver dan PyTest.

### Result

| Test Case | Result |
|---|---|
| TC-001 | PASS |
| TC-002 | PASS |
| TC-003 | PASS |
| TC-004 | PASS |
| TC-005 | PASS |

**Total: 5 Passed, 0 Failed**

---

## 2. Defect Detection

Dilakukan simulasi defect pada validasi password untuk memastikan automation dapat mendeteksi masalah pada sistem.

### Result

| Test Case | Result |
|---|---|
| TC-001 | PASS |
| TC-002 | FAIL |
| TC-003 | PASS |
| TC-004 | FAIL |
| TC-005 | PASS |

**Total: 3 Passed, 2 Failed**

### Failed Test Cases

**TC-002 - Password salah**

Expected:
`Username atau password salah`

Actual:
`Login berhasil`

**TC-004 - Password kosong**

Expected:
`Username atau password salah`

Actual:
`Login berhasil`

Defect kemudian didokumentasikan sebagai BUG-001.

---

## 3. Bug Fix

Defect diperbaiki dengan mengembalikan validasi login agar sistem memeriksa username dan password secara bersamaan.

Valid credential:

- Username: `zacky`
- Password: `123456`

---

## 4. Retesting

Setelah bug diperbaiki, test case yang sebelumnya gagal dijalankan kembali untuk memastikan defect telah diperbaiki.

Test case yang diretest:

- TC-002
- TC-004

Expected result:

Kedua test case berhasil PASS setelah perbaikan.

---

## 5. Regression Testing

Setelah retesting, seluruh test case login dijalankan kembali untuk memastikan perbaikan tidak menyebabkan masalah pada fungsi login lainnya.

### Final Result

| Test Case | Result |
|---|---|
| TC-001 | PASS |
| TC-002 | PASS |
| TC-003 | PASS |
| TC-004 | PASS |
| TC-005 | PASS |

**Total: 5 Passed, 0 Failed**

---

## 6. Final Status

Automation testing berhasil memvalidasi seluruh test case login.

Defect pada validasi password berhasil ditemukan, diperbaiki, diretest, dan diverifikasi kembali melalui regression testing.