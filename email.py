import re

email1 = "pawel.rubach@sgh.waw.pl"
email2 = "pawel.rubach@sghwaw,pl"
email3 = "@sgh.waw.pl"
email4 = "pawel@"
email5 = ""
email6 = "pawel@.pl"

emails = [email1, email2, email3, email4, email5, email6]


def check_email(email):
    if not email:
        return "Missing mail"

    if re.match("^[a-zA-Z0-9]+(?:\.[a-zA-Z0-9]+)*@gmail.com$", email):
        print(email, end=" - ")

    if email[-3:-1] == ".pl":
        print("OK", end=" - ")

    if email[:5] == "pawel":
        print("OK")





for em in emails:
    print("\"{}\" -".format(em), end=" ")
    check_email(em)
