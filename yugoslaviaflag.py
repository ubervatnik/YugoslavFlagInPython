def yugoslav_flag():
    colors = ["\033[48;5;196m", "\033[48;5;27m", "\033[48;5;255m"]  # Red, blue, and white background colors
    for i in range(1, 4):  # Keep the number of rows as before
        print(colors[i % 3] + " " * 12 + "\033[0m")

yugoslav_flag()
print("Слава Тито")