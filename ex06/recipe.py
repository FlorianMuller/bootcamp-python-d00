cookbook = {}


def add_recipe(name, ingredients, meal, prep_time):
    global cookbook

    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time
    }


def delete_recipe(name):
    global cookbook
    try:
        del cookbook[name]
        print(f"\"{name}\" deleted")
    except KeyError:
        print(f"\"{name}\" doesn't exist")


def print_recipe(name):
    if name in cookbook:
        print(
            f"Recipe for {name}:\n"
            f"- Ingredients list: {', '.join(cookbook[name]['ingredients'])}\n"
            f"- To be eaten for {cookbook[name]['meal']}\n"
            f"- Takes {cookbook[name]['prep_time']} minutes of cooking"
        )
    else:
        print(f"We don't have the recipe for \"{name}\" 🤭")


def print_all_recipe():
    for recipe in cookbook:
        print_recipe(recipe)
        print("")


def user_interface_cookbook():
    user_choice = None
    while user_choice != "5":
        if user_choice in [None, "1", "2", "3", "4", "5"]:
            user_choice = input(
                "Please select an option by typing the corresponding number:\n"
                "1: Add a recipe\n"
                "2: Delete a recipe\n"
                "3: Print a recipe\n"
                "4: Print the cookbook\n"
                "5: Quit\n"
                ">> "
            )
        else:
            user_choice = input(
                "This option does not exist, please type the corresponding"
                " number.\n"
                "To exit, enter 5.\n"
                ">> "
            )

        print("")
        if user_choice == "1":
            name = input("Name:")
            ingredients = input("Ingredients: ")
            meal = input("Meal type: ")
            prep_time = input("Time to prepare (in minutes): ")

            try:
                add_recipe(str(name), ingredients.split(", "),
                           str(meal), int(prep_time))
                print("")
            except ValueError:
                print("\nBad recipe")
                input("")
        elif user_choice == "2":
            recipe = input("What recipe do you want to delete ? 🚮\n>> ")
            print("")
            delete_recipe(recipe)
            input("")
        elif user_choice == "3":
            recipe = input("What recipe do you want to see ? 👀\n>> ")
            print("")
            print_recipe(recipe)
            input("")
        elif user_choice == "4":
            print_all_recipe()
            input("")
        elif user_choice == "5":
            print("Cookbook closed")


def mock_coockboob():
    add_recipe("sandwich", ["ham", "bread", "cheese", "tomatoes"],
               "lunch", 10)
    add_recipe("cake", ["flour", "sugar", "eggs"], "dessert", 60)
    add_recipe("salad", ["avocado", "arugula", "tomatoes", "spinach"],
               "lunch", 15)


if __name__ == "__main__":
    mock_coockboob()
    user_interface_cookbook()
