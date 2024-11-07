

# Ingredient amounts for 48 cookies


sugar = 1.5  # cups of sugar
butter = 1.0  # cup of butter
flour = 2.75  # cups of flour
cookies = 48  # number of cookies the recipe makes

# Ask the user how many cookies they want to make

desired_cookies = int(input("How many cookies do you want to make? "))

# Calculate the necessary amounts of ingredients
needed_sugar = (sugar / cookies) * desired_cookies
needed_butter = (butter / cookies) * desired_cookies
needed_flour = (flour / cookies) * desired_cookies

# Display the necessary amounts of ingredients
print(f"To make {desired_cookies} cookies, you will need:")
print(f"{needed_sugar:.2f} cups of sugar")
print(f"{needed_butter:.2f} cups of butter")
print(f"{needed_flour:.2f} cups of flour")
