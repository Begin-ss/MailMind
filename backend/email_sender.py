# backend/email_sender.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using SMTP.
    Works with Gmail (or any SMTP-based mail service).
    """

    try:
        # Create message container
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = subject

        # Attach body
        msg.attach(MIMEText(body, "plain"))

        # SMTP setup (for Gmail)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()

        print(f"✅ Email sent successfully to {recipient_email}")
        return {"status": "success", "message": f"Email sent to {recipient_email}"}

    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        return {"status": "error", "message": str(e)}
