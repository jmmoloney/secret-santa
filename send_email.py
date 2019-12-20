"""send_email.py."""
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(sender_email, password, receiver_email, message):
    """Sends email message using gmail smtp server.

    Parameters
    ----------
    sender_email : str
        Sender email address.
    password : str
        Password for sender email account.
    receiver_email : str
        Receiver email address.
    message : str
        Message header and body.

    Returns
    -------
    type
        Description of returned object.

    """
    port = 465  # For SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        msg = message.as_string()
        server.sendmail(sender_email, receiver_email, msg)


def format_message(giver, giver_email, receiver):
    """Construct the message header and body for the secret santa email.

    Parameters
    ----------
    giver : str
        Giver's name.
    giver_email : str
        Giver's email address.
    receiver : str
        Receiver's name.

    Returns
    -------
    str
        Formatted message with header and body.

    """
    msg = MIMEMultipart()
    msg["From"] = "Secret Santa"
    msg["To"] = giver_email
    msg["Subject"] = "You're the Secret Santa for ..."
    body = """Hello, {}!
            Buy this person a gift for Secret Santa: {}""".format(
        giver, receiver
    )
    msg.attach(MIMEText(body, "plain"))
    return msg
