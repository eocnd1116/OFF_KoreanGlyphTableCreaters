import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

with open("EN.txt", "r", encoding="utf-8", newline='') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    for row in reader:
        ws.append(row)

wb.save("result.xlsx")
