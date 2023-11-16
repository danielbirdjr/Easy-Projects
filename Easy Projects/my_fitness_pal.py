#Food & nutrtion info library
food_database = {
    "ground beef": {
        "serving_size": "1 oz", 
        "calories": 50, 
        "protein": 5.8, 
        "carbs": 0, 
        "fat": 2.8, 
        "cost_per_unit": 3.88/16, # $3.88 / lb
        "store": "Sam's Club"
    }, 
    "egg": {
        "serving_size": "1 egg", # large egg
        "calories": 78, 
        "protein": 6.3, 
        "carbs": 0.6, 
        "fat": 5.3, 
        "cost_per_unit": 2.00/12, # $2.00 / dozen 
        "store": "Local farm"
    }, 
    "salmon": {
        "serving_size": "1 oz", 
        "calories": 31, 
        "protein": 6, 
        "carbs": 0, 
        "fat": 1, 
        "cost_per_unit": 6.20/16, # $6.20 / lb 
        "store": "Aldi's"
    }, 
    "rice": {
        "serving_size": "1 oz (dry)", #white rice
        "calories": 112, 
        "protein": 2.3, 
        "carbs": 24.3, 
        "fat": 0.2, 
        "cost_per_unit": 12.98/(25*16), # $12.98 / 25 lb 
        "store": "Sam's Club"
    }
}

food_items_info = []

while True: 
    food_name = input("\nEnter food: ").lower()

    if food_name not in food_database: 
        print("Food not found.")
        continue

    while True: 
        try: 
            food_quantity = float(input("Quantity: "))
            if food_quantity < 0: 
                print("Enter a positive quantity.")
                continue
            break
        except ValueError: 
            print("Enter a valid number.")
            
    food_info = food_database[food_name]
    calories = food_info["calories"] * food_quantity
    protein = food_info["protein"] * food_quantity
    carbs = food_info["carbs"] * food_quantity
    fat = food_info["fat"] * food_quantity
    cost = food_info["cost_per_unit"] * food_quantity

    food_items_info.append({
        "food_name": food_name, 
        "quantity": food_quantity,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat,
        "cost": cost
    })

    while True: 
        another_food = input("Do you want to add another food (Y/N): ")

        if another_food == 'n':
            break
        elif another_food == 'y':
            break
        else: 
            print("Enter 'Y' or 'N'.")

    if another_food == 'n':
        break

total_calories = sum(item["calories"] for item in food_items_info)
total_protein = sum(item["protein"] for item in food_items_info)
total_carbs = sum(item["carbs"] for item in food_items_info)
total_fat = sum(item["fat"] for item in food_items_info)
total_cost = sum(item["cost"] for item in food_items_info)

print("\nTotal of all foods")
print(f"{total_calories:.0f} calories")
print(f"{total_protein:.0f} g protein")
print(f"{total_carbs:.0f} g carbs")
print(f"{total_fat:.0f} g fat")
print(f"${total_cost:.2f}\n")

while True:
    shopping_option = input("Do you want to see what to get for the week when shopping (Y/N): ").lower()
    if shopping_option == 'y':
        store_weekly_totals = {} #store weekly totals for each store

        for item in food_items_info: 
            food_name = item["food_name"]
            food_quantity = item["quantity"]
            store = food_database[food_name]["store"]

            if store not in store_weekly_totals: 
                store_weekly_totals[store] = {}

            if food_name in store_weekly_totals[store]: 
                store_weekly_totals[store][food_name] += food_quantity
            else: 
                store_weekly_totals[store][food_name] = food_quantity

        print("\nWeekly Shopping List:")
        for store, items in store_weekly_totals.items():
            print(f"\n{store}")
            for food_name, quantity in items.items():
                print(f"{quantity * 7} {food_name}")

        break
    if shopping_option == 'n':
        print()
        break
    else: 
        print("Enter 'Y' or 'N'.")