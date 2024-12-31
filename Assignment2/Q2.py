answer = input("Is it raining? (yes/no): ").strip().lower()

if answer == "yes":
    print("Carry an umbrella.")
elif answer == "no":
    print("No need to carry an umbrella.")
else:
    print("Bye.")
