import sys

def create_inventory(): #el parseo
    inventory = {}
    params = sys.argv[1:] #NO TIENES Q RECORRELOS Y METERLOS?
    for p in params:
        if ":" not in p:
            print(f"Error- invalid parameter '{p}'")
            continue

        item, qty = p.split(":", 1)

        #Redundante
        if item in inventory :
            print(f"Redundant item '{item}'- discarding")
            continue

        #Cantidad invalida
        try:
            qty = int(qty)
        except Exception as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory[item] = qty

    return inventory

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory = create_inventory()
    print(f"Got inventory: {inventory}") #show the entire inventory
    items = list(inventory.keys())       #show only de keys
    print(f"Item list: {inventory.keys()}")      

    #suma de los objetos
    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    #porcentaje de lo q representa en el inventario
    for item, qty in inventory.items():
        percent = (qty / total) * 100
        print(f"Item {item} represents {percent:.1f}%")

    #item mas y menos abundante
    most_item = max(inventory, key = lambda x: inventory[x])
    print(f"Item most abundant: {most_item} with quantity {inventory[most_item]}")

    least_item = min(inventory, key = lambda x: inventory[x])
    print(f"Item least abundant: {least_item} with quantity {inventory[least_item]}")

    #añadir un nuevo item
    inventory.update({"magic_item": 1}) 
    print("Updated inventory:", inventory)