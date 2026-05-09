import math

def get_player_pos():
    while (True):
        enter = input("Enter new coordinates as floats in format 'x, y, z': ")
        parts = enter.split(",")

        if (len(parts) != 3):
            print("Invalid syntax")
            continue
        
        cordinates = []

        for i in parts:
            try:
                cor_num = float(i)
                cordinates.append(cor_num)
            except ValueError as e:
                print(f"Error on parameter '{i}' : {e}")
                break
        if (len(cordinates) == 3):
            return cordinates


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    cordinates = get_player_pos()
    print(f"Got a first tuple: {tuple(cordinates)}")
    x, y, z = cordinates
    print(f"It includes: X={x}, Y={y}, Z={z}")
    print(f"Distance to center:")
    dist = math.sqrt(x*x + y*y + z*z)
    print(f"Distance to center: {round(dist, 4)}")

    print()
    print("Get a second set of coordinates")
    second_cordinates = get_player_pos()
    x1, y1, z1 = cordinates
    x2, y2, z2 = second_cordinates
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between the 2 sets of coordinates: {distance}")