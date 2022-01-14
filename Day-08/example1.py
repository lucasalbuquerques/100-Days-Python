def greet():
    print("Hello")
    print("How do you do? ")
    print("Isn't the weather nice today? ")

greet()

def greet_with_name(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

    
greet_with_name("Lucas", "Porto Alegre") 
print()
greet_with_name(name = "Lucas", location = "Porto Alegre") 