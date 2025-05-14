import re

def extract_brands(text):
    lines = text.split("\n")
    brand_data = []
    for line in lines:
        match = re.match(r"\s*\d+[\.\):\-]?\s*(.*?):\s*(.*)", line)
        if match:
            brand, reason = match.groups()
            brand_data.append({"brand": brand.strip(), "reason": reason.strip()})
    return brand_data
