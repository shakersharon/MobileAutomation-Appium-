# Mobile App Automation Testing Project

**Tech Stack**: Appium + Python + Pytest

**Target App**: [ApiDemos-debug.apk](https://github.com/appium/appium/raw/master/packages/appium/sample-code/apps/ApiDemos-debug.apk
)


## 📄 `config/capabilities.json`

```json
{
  "android_apidemos": {
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "deviceName": "emulator-5554",
    "app": "apps/ApiDemos-debug.apk",
    "appPackage": "io.appium.android.apis",
    "appActivity": "io.appium.android.apis.ApiDemos"
  }
}
```

---

## 🧪 Test Coverage Summary

- ✅ Functional Test (Text Logging, Input Field)
- ✅ Form Validation (Empty field behavior)
- ✅ Login (Data-driven)
- ✅ Gestures (Swipe)
- ✅ Visual Testing (Screenshot comparison)
- ✅ Accessibility (Content description check)
- ✅ Performance (App launch time)

---

## ▶️ How to Run Tests

```bash
# Step 1: Start Appium server
appium

# Step 2: Launch Android emulator or connect real device

# Step 3: Install Python dependencies
pip install -r requirements.txt

# Step 4: Run all tests
pytest --device=android_apidemos
```

---

## 💡 Tips

- Use `--device=<name>` to switch capabilities if you add more profiles in `capabilities.json`
- Store all screenshots in `screenshots/`
- Add more test suites under the `tests/` folder to scale the test coverage

---

## 📦 `requirements.txt`

```
pytest
Appium-Python-Client
```
## 📦 `▶️ How to Run`

```
# 1. Start Appium Server
appium

# 2. Launch emulator or connect real device

# 3. Run all tests
pytest --device=android_apidemos

# 4. Run only single test
pytest tests/functional/test_text_log.py
```

---

## 🔢 Sample Login Data (`config/login_data.json`)

```json
[
  {"username": "user1", "password": "pass1"},
  {"username": "admin", "password": "admin123"},
  {"username": "test", "password": "test"}
]
```
