import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, to_emails):
    try:
        # Get environment variables
        sender_email = os.getenv("SENDER_EMAIL")
        sender_password = os.getenv("SENDER_PASSWORD")
        email_host = os.getenv("EMAIL_HOST")
        email_port = os.getenv("EMAIL_PORT")

        # Create a multipart message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = ", ".join(to_emails.split(","))
        msg["Subject"] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, "html"))

        # Create SMTP session
        with smtplib.SMTP(email_host, email_port) as server:
            server.ehlo()
            # Start TLS for security
            server.starttls()
            # Authentication
            server.login(sender_email, sender_password)
            # Sending the mail
            server.sendmail(sender_email, to_emails.split(","), msg.as_string())
            print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")


def get_html_template(table_rows: str) -> str:
    return (
        """
    <!DOCTYPE html>
    <html >
    <head>
    <style>
        table {
        font-family: Arial, sans-serif;
        border-collapse: collapse;
        width: 100%;
        }

        td, th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
        }

        tr:nth-child(even) {
        background-color: #f2f2f2;
        }
    </style>
    </head>
    <body>
    <h2>Price Drop Alert</h2>
    <p>Hey Buyers,</p>
    <p>Below are the products with price drop:</p>
    <table>
        <tr>
        <th>Product</th>
        <th>Current Price</th>
        <th>Target Price</th>
        <th>Link</th>
        </tr>
        """
        + table_rows
        + """
    </table>
    <p>Best,</p>
    <p>Price Drop Alert System</p>
    </body>
    </html>
    """
    )
