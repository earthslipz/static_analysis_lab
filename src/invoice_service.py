from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple

@dataclass
class LineItem:
    sku: str
    category: str
    unit_price: float
    qty: int
    fragile: bool = False

@dataclass
class Invoice:
    invoice_id: str
    customer_id: str
    country: str
    membership: str
    coupon: Optional[str]
    items: List[LineItem]

class InvoiceService:
    def compute_total(self, inv: Invoice) -> Tuple[float, List[str]]:
        subtotal = sum(it.unit_price * it.qty for it in inv.items)
        # ตัวอย่างโค้ดที่มีความซับซ้อน (Nesting) เพื่อให้ Sonar ตรวจเจอ
        shipping = 0
        if inv.country == "TH":
            shipping = 60 if subtotal < 500 else 0
        return subtotal + shipping, []
