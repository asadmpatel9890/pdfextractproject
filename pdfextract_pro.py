import re
from pdfminer.high_level import extract_pages,extract_text

# for page_layout in extract_pages("Sample.pdf"):
#     for element in page_layout:
#         print(element)

text = extract_text("Sample.pdf")

pattern = re.compile(r"[a-zA-Z]+")
matches = pattern.findall(text)

print(matches)