
def get_player_pos():
    print("Get a first set of coordinates")
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
            except ErrorValue as e:
                print(f"Error on parameter '{i}' : {e}")
                break
        if (len(cordinates) == 3):
            print(f"Got a first tuple: ({print(cordinates)})")
            return cordinates


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    cordinates = get_player_pos()