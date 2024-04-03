print('__name__:', __name__)

def square(x):
  return x * x

def calculator(a, b, operator):
  if operator == '+':
    return a + b
  elif operator == '-':
    return a - b
  elif operator == '*':
    return a * b
  elif operator == '/':
    return a / b
  else:
    return None

def main():
  print(calculator(1, 2, '+'))
  print(calculator(1, 2, '-'))
  print(calculator(1, 2, '*'))
  print(calculator(1, 2, '/'))
  print(square(5))
  
if __name__ == "__main__":
  main()