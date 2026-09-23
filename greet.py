import os

name = input("What is your name? ")
print(f"Hello, {name}!")

# This line triggers your Mac to say hello out loud using your name!
os.system(f'say "Hello {name}"')


