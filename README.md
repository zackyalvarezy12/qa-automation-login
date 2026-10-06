# QA Automation - HRIS Login Testing

Project ini merupakan portfolio QA Automation yang dibuat untuk menguji fitur Login pada sistem sederhana.

Pengujian dilakukan menggunakan Selenium WebDriver dan PyTest dengan pendekatan functional testing, negative testing, defect detection, retesting, dan regression testing.

## Objective

Tujuan project ini adalah:

- Membuat test scenario dan test case
- Melakukan automation testing menggunakan Selenium
- Menjalankan test menggunakan PyTest
- Menemukan defect pada sistem
- Membuat bug report
- Melakukan retesting setelah bug diperbaiki
- Melakukan regression testing
- Mendokumentasikan hasil pengujian

## Technology

- Python 3.14
- Selenium 4.50.0
- PyTest 9.1.1
- Google Chrome
- HTML & JavaScript

## Test Scenarios

| ID | Scenario |
|---|---|
| TS-001 | Login dengan credential valid |
| TS-002 | Login dengan password salah |
| TS-003 | Login dengan username kosong |
| TS-004 | Login dengan password kosong |
| TS-005 | Login dengan username dan password kosong |

## Test Cases

Total test case: **5**

| ID | Test Case | Expected Result |
|---|---|---|
| TC-001 | Login valid | Login berhasil |
| TC-002 | Password salah | Username atau password salah |
| TC-003 | Username kosong | Username wajib diisi |
| TC-004 | Password kosong | Username atau password salah |
| TC-005 | Username dan password kosong | Username wajib diisi |

## Automation Testing

Test automation dibuat menggunakan Selenium WebDriver dan PyTest.

Test dijalankan menggunakan:

```bash
python -m pytest -v