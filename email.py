import re

email1 = "ostap.komar7@gmail.com"
email2 = "ostap.@gmail.com"
email3 = "ostap%gmail.com"
email4 = "ostap@gmail.net"
email5 = ""
email6 = "ostap.komar"

emails = [email1, email2, email3, email4, email5, email6]


def check_email(email):
    if not email:
        return "Missing mail"

    if re.match("^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@gmail.com$", email):
        print(email, end=" - ")

    if email[-3:-1] == "com":
        print("OK", end=" - ")

    if email[:5] == "ostap":
        print("OK")

    return True




for em in emails:
    print("\"{}\" -".format(em), end=" ")
    check_email(em)
