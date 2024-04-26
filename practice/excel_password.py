# access excel file on my mac and then try to open it with password
# if the password is correct then print the password

import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('path_to_your_file.xlsx')

# Access a specific worksheet
worksheet = workbook['SheetName']

# Check if the worksheet is protected
if worksheet.protection.sheet:
    print("The worksheet is protected.")
else:
    print("The worksheet is not protected.")

# Attempting to modify a protected worksheet will raise an error unless it is unprotected
try:
    worksheet['A1'] = "New Value"  # This will fail if the worksheet is protected
except AttributeError as e:
    print("Failed to modify the worksheet:", e)

# Unprotect the worksheet with the password
worksheet.protection.disable()
worksheet.password = None  # Clear the password if you wish

# Now you should be able to edit the worksheet
worksheet['A1'] = "New Value"
