from .models import Bill

def generate_bill_no():
    last_bill = Bill.objects.all().order_by("id").last()
    if last_bill:
        last_no = int(last_bill.bill_no.split("-")[-1])
        return f"BILL-{last_no+1:04d}"
    return "BILL-0001"


