# access excel file on my mac and then try to open it with password
# if the password is correct then print the password

import openpyxl

def open_excel_file(file_path):
    try:
        workbook = openpyxl.load_workbook(file_path)
        print("File loaded")
        print(workbook)
    except openpyxl.utils.exceptions.InvalidFileException:
        print("File did not load")
    except Exception as e:
        print("An error occurred:", e)
        
def main():
    file_path = "/Users/johndunn/Downloads/excel_test/test-no-macros.xlsx"
    open_excel_file(file_path)
    
if __name__ == "__main__":
    main()