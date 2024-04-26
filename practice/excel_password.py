# access excel file on my mac and then try to open it with password
# if the password is correct then print the password

import openpyxl

wb = openpyxl.load_workbook('/Users/..', read_only=False)

print(wb.sheetnames)
