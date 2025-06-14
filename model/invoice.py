from model.booking import Booking

class Invoice:
    def __init__(self, invoice_id, booking: Booking, issue_date, total_amount):
        self.invoice_id = invoice_id
        self.booking = booking
        self.issue_date = issue_date
        self.total_amount = total_amount

    def __str__(self):
        return f"Invoice #{self.invoice_id} | Booking #{self.booking.booking_id} | Total: ${self.total_amount:.2f} | Issued: {self.issue_date}"
