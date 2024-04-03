from calculator import square

def main():
  test_square_basic()
  
def test_square_basic():
  assert square(5) == 25
  assert square(0) == 0
  assert square(-5) == 25
  assert square(2.5) == 6.25
  
if __name__ == "__main__":
  main()
  
# Execute file by running pytest [relative path to file] in the terminal