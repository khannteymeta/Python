# Data structure

# List data structure
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)


age = [25, 30, 35, 40, 45]
print("Ages:", age)


day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Insert at specific position # syntax:insert(index, value)
day.insert(2, "Sunday")

# Add to the last position
oppend_day = day.append("Saturday")


# Remove an item
day.remove("Sunday")

# Pop an item
popped_day = day.pop(3)  # Removes "Thursday"

print("Days of the week:", day)


