import csv

def open_csv_vanilla():
  with open('practice/students.csv') as file:
    for line in file:
      row = line.rstrip().split(',')
      print(f'{row[0]} is in {row[1]}')
      # can also use array destructuring
      name, course = line.rstrip().split(',')
      print(f'{name} is in {course}')
    
def open_csv():
  with open('practice/students.csv') as file:
    reader = csv.reader(file)
    for row in reader:
      # print(row)
      print(f'{row[0]} is in {row[1]}')
    
def main():
  # open_csv_vanilla()
  open_csv()
      
if __name__ == '__main__':
  main()