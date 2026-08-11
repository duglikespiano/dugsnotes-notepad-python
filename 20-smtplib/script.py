"""
smtplib in Python
=================

smtplib is a built-in Python module used to send emails through
an SMTP (Simple Mail Transfer Protocol) server.

SMTP is the protocol commonly used for sending email.

Basic flow:

    Python program
        |
        v
    SMTP server
        |
        v
    Recipient's email server
        |
        v
    Recipient's inbox


IMPORTANT:
- Never put your real email password directly into source code.
- For real applications, use environment variables or a secret manager.
"""

import smtplib
from email.message import EmailMessage

# ============================================================
# 1. BASIC SMTP CONCEPTS
# ============================================================

"""
An SMTP server is a server that accepts outgoing email.

Common SMTP servers include:

    Gmail:
        smtp.gmail.com
        Port 587 -> STARTTLS
        Port 465 -> SSL

    Outlook / Microsoft:
        smtp.office365.com
        Port 587 -> STARTTLS

The exact settings depend on your email provider.
"""


# ============================================================
# 2. SIMPLE EMAIL EXAMPLE
# ============================================================

"""
This example shows the general structure.

Do NOT put your real password into a Python file like this:

    password = "my_real_password"

Instead, use an environment variable.
"""


sender = "your_email@example.com"
recipient = "recipient@example.com"

# This is only a placeholder.
# Do not replace this with your real password in production.
password = "YOUR_PASSWORD"


message = EmailMessage()

message["From"] = sender
message["To"] = recipient
message["Subject"] = "Hello from Python"

message.set_content("Hello!\n\n" "This email was sent using Python's smtplib module.\n")


"""
Now we connect to the SMTP server.

For Gmail using STARTTLS:

    smtp.gmail.com
    port 587
"""

# The following code is an example.
# It will not work until you provide valid SMTP credentials.

# with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#     smtp.starttls()
#     smtp.login(sender, password)
#     smtp.send_message(message)


# ============================================================
# 3. UNDERSTANDING THE SMTP CONNECTION
# ============================================================

"""
This:

    smtplib.SMTP("smtp.gmail.com", 587)

creates a connection to the SMTP server.

Port 587 is commonly used for SMTP with STARTTLS.

Then:

    smtp.starttls()

upgrades the connection to an encrypted TLS connection.

Then:

    smtp.login(sender, password)

authenticates your account.

Finally:

    smtp.send_message(message)

sends the email.
"""


# ============================================================
# 4. COMPLETE SEND_EMAIL FUNCTION
# ============================================================


def send_email(sender, password, recipient, subject, body):
    """
    Send a plain-text email.

    Parameters:
        sender:
            Email address sending the message.

        password:
            Password or app password for the SMTP account.

        recipient:
            Email address receiving the message.

        subject:
            Email subject.

        body:
            Email body.
    """

    message = EmailMessage()

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    message.set_content(body)

    # Connect to the SMTP server.
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        # Encrypt the connection using TLS.
        smtp.starttls()

        # Log in to the SMTP server.
        smtp.login(sender, password)

        # Send the email.
        smtp.send_message(message)


"""
Example usage:

    send_email(
        sender="your_email@gmail.com",
        password="YOUR_APP_PASSWORD",
        recipient="friend@example.com",
        subject="Test Email",
        body="Hello from Python!"
    )

Again, do not put your real password directly into source code.
"""


# ============================================================
# 5. USING ENVIRONMENT VARIABLES
# ============================================================

"""
A better approach is to store sensitive information in
environment variables.

For example:

    EMAIL_ADDRESS
    EMAIL_PASSWORD

Then Python can read them using os.getenv().
"""

import os

email_address = os.getenv("EMAIL_ADDRESS")
email_password = os.getenv("EMAIL_PASSWORD")


"""
For example, you could write:

    email_address = os.getenv("EMAIL_ADDRESS")

If the environment variable contains:

    EMAIL_ADDRESS=example@gmail.com

then:

    email_address

will contain:

    "example@gmail.com"
"""


# ============================================================
# 6. SAFER EMAIL FUNCTION
# ============================================================


def send_email_with_environment_variables(recipient, subject, body):
    """
    Send an email using credentials stored in environment variables.
    """

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    if not sender or not password:
        raise ValueError("EMAIL_ADDRESS and EMAIL_PASSWORD must be set.")

    message = EmailMessage()

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject

    message.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)


# ============================================================
# 7. MULTIPLE RECIPIENTS
# ============================================================

"""
You can send an email to multiple recipients.

One way is to provide a list of addresses.
"""


def send_to_multiple_recipients(sender, password, recipients, subject, body):
    """
    Send one email to multiple recipients.

    recipients should be a list, for example:

        [
            "alice@example.com",
            "bob@example.com",
            "charlie@example.com"
        ]
    """

    message = EmailMessage()

    message["From"] = sender

    # Join the list into a comma-separated string.
    message["To"] = ", ".join(recipients)

    message["Subject"] = subject

    message.set_content(body)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)


# ============================================================
# 8. CC AND BCC
# ============================================================

"""
EmailMessage also supports:

    To
    Cc
    Bcc
"""


def send_email_with_cc_and_bcc(sender, password):
    message = EmailMessage()

    message["From"] = sender

    message["To"] = "recipient@example.com"

    message["Cc"] = "manager@example.com"

    # Bcc recipients receive the email but are hidden
    # from other recipients.
    message["Bcc"] = "admin@example.com"

    message["Subject"] = "Email with CC and BCC"

    message.set_content("This email demonstrates To, Cc, and Bcc.")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)


# ============================================================
# 9. HTML EMAIL
# ============================================================

"""
EmailMessage can contain HTML.

For example, instead of sending only plain text,
we can send an HTML email.
"""


def send_html_email(sender, password, recipient):
    message = EmailMessage()

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = "HTML Email from Python"

    # Plain-text fallback.
    message.set_content(
        "This email contains HTML. " "Please use an HTML-capable email client."
    )

    # HTML version.
    html = """
    <html>
        <body>
            <h1>Hello!</h1>

            <p>
                This email was sent using
                <strong>Python</strong>.
            </p>

            <p>
                This is an HTML email.
            </p>
        </body>
    </html>
    """

    message.add_alternative(html, subtype="html")

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)


# ============================================================
# 10. SENDING AN ATTACHMENT
# ============================================================

"""
EmailMessage can also send files as attachments.

For example, suppose you have:

    report.pdf

in the same directory as your Python script.
"""


def send_attachment(sender, password, recipient):
    message = EmailMessage()

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = "Report"

    message.set_content("Hello,\n\n" "Please find the report attached.\n")

    # Open the file in binary mode.
    with open("report.pdf", "rb") as file:
        file_data = file.read()

    message.add_attachment(
        file_data, maintype="application", subtype="pdf", filename="report.pdf"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)


# ============================================================
# 11. SMTP WITH SSL
# ============================================================

"""
There are two common approaches:

    STARTTLS:
        smtplib.SMTP(...)
        smtp.starttls()

    SSL:
        smtplib.SMTP_SSL(...)

For example, Gmail commonly supports:

    smtp.gmail.com
    port 465
"""


def send_email_with_ssl(sender, password, recipient):
    message = EmailMessage()

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = "SMTP SSL Test"

    message.set_content("This email uses an SSL SMTP connection.")

    # SMTP_SSL creates an encrypted connection immediately.
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(message)


# ============================================================
# 12. ERROR HANDLING
# ============================================================

"""
SMTP operations can fail.

For example:

    - Incorrect username/password
    - SMTP server unavailable
    - Network problem
    - Authentication failure
    - Invalid recipient
    - Connection timeout

You can use try/except to handle errors.
"""


def send_email_safely(sender, password, recipient):
    message = EmailMessage()

    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = "Safe SMTP Example"

    message.set_content("This email demonstrates error handling.")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(message)

        print("Email sent successfully.")

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed.")

    except smtplib.SMTPException as error:
        print(f"SMTP error: {error}")

    except OSError as error:
        print(f"Network or connection error: {error}")


# ============================================================
# 13. IMPORTANT METHODS
# ============================================================

"""
Here are some of the most important smtplib methods:

    smtplib.SMTP()
        Create an SMTP connection.

    smtplib.SMTP_SSL()
        Create an SMTP connection using SSL.

    smtp.starttls()
        Upgrade the connection to TLS encryption.

    smtp.login()
        Authenticate with the SMTP server.

    smtp.sendmail()
        Send an email using raw email data.

    smtp.send_message()
        Send an email.message.EmailMessage object.

    smtp.quit()
        Close the SMTP connection.

Using "with" is usually better because the connection
is automatically cleaned up.
"""


# ============================================================
# 14. sendmail() VS send_message()
# ============================================================

"""
There are two commonly encountered sending methods.

sendmail():

    smtp.sendmail(
        sender,
        recipient,
        message
    )

send_message():

    smtp.send_message(message)

send_message() works naturally with EmailMessage and is
usually easier to use for modern Python email code.

For example:
"""


def sendmail_example(sender, password, recipient):
    message = (
        "From: " + sender + "\n"
        "To: " + recipient + "\n"
        "Subject: sendmail example\n"
        "\n"
        "Hello from Python!"
    )

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)

        smtp.sendmail(sender, recipient, message)


# ============================================================
# 15. SIMPLE MENTAL MODEL
# ============================================================

"""
Think about sending an email as these steps:

    1. Create the email
           |
           v
    2. Connect to SMTP server
           |
           v
    3. Encrypt the connection
           |
           v
    4. Log in
           |
           v
    5. Send the message
           |
           v
    6. Close the connection


In code:

    message = EmailMessage()

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(message)


That is the core pattern you should remember.
"""


# ============================================================
# 16. MINIMAL EXAMPLE TO REMEMBER
# ============================================================

"""
The most important example:

    import smtplib
    from email.message import EmailMessage

    message = EmailMessage()

    message["From"] = "sender@example.com"
    message["To"] = "recipient@example.com"
    message["Subject"] = "Hello"

    message.set_content("Hello from Python!")

    with smtplib.SMTP("smtp.example.com", 587) as smtp:
        smtp.starttls()
        smtp.login("sender@example.com", "PASSWORD")
        smtp.send_message(message)


Remember:

    EmailMessage
        -> creates the email

    smtplib.SMTP
        -> connects to the SMTP server

    starttls()
        -> enables TLS encryption

    login()
        -> authenticates

    send_message()
        -> sends the email
"""


# ============================================================
# 17. IMPORTANT SECURITY NOTE
# ============================================================

"""
NEVER commit credentials to Git.

Bad:

    password = "my-real-password"

Better:

    password = os.getenv("EMAIL_PASSWORD")

You can also use a .env file with a package such as python-dotenv,
but make sure the .env file is included in .gitignore.

For Gmail and other providers, you may need an app password
or another supported authentication method rather than your
normal account password.

Always check your email provider's current SMTP authentication
requirements.
"""


# ============================================================
# END
# ============================================================

"""
Summary:

    smtplib
        = Python's standard library for SMTP communication.

    EmailMessage
        = convenient way to construct an email.

    SMTP
        = connect to an SMTP server.

    SMTP_SSL
        = connect using SSL.

    starttls()
        = encrypt an SMTP connection using TLS.

    login()
        = authenticate with the SMTP server.

    send_message()
        = send an EmailMessage.

    add_alternative()
        = add HTML email content.

    add_attachment()
        = attach a file.

The basic pattern is:

    create message
    -> connect
    -> encrypt
    -> authenticate
    -> send
    -> close
"""
