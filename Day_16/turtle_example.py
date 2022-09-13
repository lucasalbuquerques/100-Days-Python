import turtle
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.color("blue")
# timmy.shape("turtle")
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)