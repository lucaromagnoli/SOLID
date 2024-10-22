"""Single Responsibility Principle.

A class should have only one reason to change, meaning that a class should have only one job.

E.g. A class that is responsible for sending emails should not be responsible for formatting the email.
"""
class EmailSender:
    def send_email(self, email, message):
        pass


class EmailFormatter:
    def format_email(self, email, message):
        pass
    