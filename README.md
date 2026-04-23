# 📧 Email Validator (Python)

A simple Python project that validates email addresses using basic **string operations**.
This project is beginner-friendly and helps understand conditions, string methods, and input handling.

---

## 🚀 Features

* Checks if email contains exactly one `@`
* Ensures at least one `.` is present
* Validates minimum length (> 6 characters)
* Optionally checks if email ends with `.com`
* Uses only **core Python (no libraries)**

---

## 🧠 Concepts Used

* String methods (`count()`, `endswith()`, `isalpha()`)
* Conditional statements (`if-else`)
* Boolean logic
* User input handling

---

## 📂 Project Structure

```
email-validator/
│── main.py
│── README.md
```

---

## ▶️ How to Run

1. Make sure you have Python installed
2. Run the file:

```bash
python main.py
```

3. Enter your email when prompted

---

## 💻 Example

```
Enter your email: test@gmail.com
Valid email
```

```
Enter your email: testgmail.com
Invalid email address. it should contain '@' one time.
```

---

## 🧾 Code

```python
email = str(input("Enter your email: "))

if ("@" in email) and email.count("@") == 1 and "." in email and email.count(".") >= 1:
    if len(email) > 6:
        if email.endswith(".com"):
            print("Valid email")
        else:
            print("Invalid email. Must end with .com")
    else:
        print("Invalid email address. it should be at least 6 characters long.")
else:
    print("Invalid email address. it should contain '@' one time.")
```

---

## ⚠️ Limitations

* Only supports `.com` emails
* Does not fully follow real-world email standards
* Allows some invalid formats (basic validation only)

---

## 🔥 Future Improvements

* Add support for `.org`, `.net`, etc.
* Use **Regex** for advanced validation
* Create GUI version (Tkinter or Web-based)
* Convert into API using Flask / FastAPI

---

## 👨‍💻 Author

Made with ❤️ by *Arshu (The Quiet Coder)*

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
