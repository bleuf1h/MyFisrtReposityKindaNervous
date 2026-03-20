#REAL OR FAKE DORITO
import time

def get_side(number):
    while True:
        try:
            value = int(input(f"Enter the length of side {number}: "))
            if value <= 0:
                print("Error: Side must be a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a numeric value.")
        except Exception as e:
            print("Algo salio mal")

def is_real_dorito(a, b, c):
    sides = [a, b, c]
    sides.sort()
    print(f"Sides in order ig: {sides[0]}, {sides[1]}, {sides[2]}")
    return sides[0] + sides[1] > sides[2]

n1 = get_side(1)
n2 = get_side(2)
n3 = get_side(3)

print("Calculating...")
time.sleep(1)

if is_real_dorito(n1, n2, n3):
    print(f"The dorito with sides {n1}, {n2}, and {n3} is a real dorito!")
else:
    print(f"The dorito with sides {n1}, {n2}, and {n3} is not a real dorito (where did u buy that bro??)")
