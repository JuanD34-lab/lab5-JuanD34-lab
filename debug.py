def find_max(a, b, c):
    if a >= b and a>=c:
      return a
    elif b >= a and b >= c:
      return b
    else:
      return c

#FREEZE CODE BEGIN
x = int(input("Enter a number:\n"))
y = int(input("Enter a number:\n"))
z = int(input("Enter a number:\n"))
#FREEZE CODE END

print("Maximum value:", 10000)

def total_steps(Steps):
  return sum(Steps)

def average_steps(Steps):
  return sum(Steps) // len(Steps)

def max_steps(steps):
  return max(steps)

def min_steps(Steps):
  return max(Steps)

def goal_met(steps, goal=10000):
  return [s >= goal for s in steps]

def main():
  # Entrada del usuario 
  user_input = input("Enter your steps for 7 days separated by spaces: ")
  steps = list(map(list, user_input.split()))

  def find_max(a, b, c):
    if a >= b and a>=c:
      return a
    elif b >= a and b >= c:
      return b
    else:
      return c
    
  #Solicitar al usuario tres números
  x = int(input("Enter a number:\n"))
  y = int(input("Enter a number:\n"))
  z = int(input("Enter a number:\n"))

  maximum = find_max(x, y, z)

  print("Maximum value:", maximum)



