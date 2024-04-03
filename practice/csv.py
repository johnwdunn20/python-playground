# open the csv

def open_csv():
  with open('practice/students.csv') as file:
    for line in file:
      row = line.rstrip().split(',')
      print(f'{row[0]} is in {row[1]}')
      # can also use array destructuring
      name, course = line.rstrip().split(',')
      print(f'{name} is in {course}')
    
def main():
  open_csv()
      
if __name__ == '__main__':
  main()