import ssl
import smtplib
from django.core.mail.backends.smtp import EmailBackend


class CustomEmailBackend(EmailBackend):
    """
    Custom SMTP email backend that disables SSL certificate verification
    for Python 3.13 compatibility with Gmail on Windows.
    """

    def open(self):
        """
        Attempt to open a connection to the SMTP server.
        Return whether or not the connection was successful.
        """
        if self.connection is not None:
            # Already open
            return False

        try:
            # Create SSL context that ignores certificate verification
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE

            connection_class = smtplib.SMTP_SSL if self.use_ssl else smtplib.SMTP

            if self.use_ssl:
                self.connection = connection_class(
                    self.host, self.port, context=ssl_context, timeout=self.timeout
                )
            else:
                self.connection = connection_class(
                    self.host, self.port, timeout=self.timeout
                )

            # Set encryption (if not already using SMTP_SSL)
            if self.use_tls:
                self.connection.starttls(context=ssl_context)

            if self.username and self.password:
                self.connection.login(self.username, self.password)

            return True
        except Exception as e:
            if not self.fail_silently:
                raise
            return False
