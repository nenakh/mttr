#!/usr/bin/env python3

import pymupdf as pymp
import re
from bs4 import BeautifulSoup as soupify

pymp_doc = pymp.open("/Users/nenakh/HIRN/methlehr_1_VL_03.pdf")

# TODO 
# - Turn first page into H1.
# - Turn page into image and include as part of text.
#

for page_number, page in enumerate(pymp_doc):
    soup = soupify(page.get_text("html"), "html.parser")
    
    if page_number == 0:
        

    for b in soup.find_all("b"):
        b.string = f"**{b.text.strip()}**"

    for i, span in enumerate(soup.find_all("span")):
        style = span.get("style", "")
        font_size = float(style.split("font-size:")[1].split("pt;")[0])
        if font_size > 25 and i < 3:
            span.string = f"## {span.text.strip()}"

    for p in soup.find_all("p"):
        p.insert_after("\n\n")



    #page_content = re.sub(r"(?<=\n).{1,3}(?=\n)", "", page_content)
    #age_content = re.sub(r"^.*?\n(.*?)\n", r"## \1 \n\n", page_content)
