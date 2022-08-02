import uuid

def generte_order_code() -> str:
    code = str(uuid.uuid4()).replace("-","")[:6]
    return f"chimeal-{code}"
 