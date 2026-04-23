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