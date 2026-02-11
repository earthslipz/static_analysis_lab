from invoice_service import InvoiceService, Invoice, LineItem
def test_basic():
    service = InvoiceService()
    inv = Invoice("I1", "C1", "TH", "none", None, [LineItem("A", "food", 100, 1)])
    total, _ = service.compute_total(inv)
    assert total == 160
