# Test Cases - HRIS Login

| Test Case ID | Test Scenario | Test Data | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-001 | Login dengan username dan password valid | zacky / 123456 | Login berhasil | Login berhasil | PASS |
| TC-002 | Login dengan password salah | zacky / salah123 | Username atau password salah | Username atau password salah | PASS |
| TC-003 | Login dengan username kosong | kosong / 123456 | Username wajib diisi | Username wajib diisi | PASS |
| TC-004 | Login dengan password kosong | zacky / kosong | Username atau password salah | Username atau password salah | PASS |
| TC-005 | Login dengan username dan password kosong | kosong / kosong | Username wajib diisi | Username wajib diisi | PASS |