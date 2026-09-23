import random
import string
import subprocess

def copy_to_clipboard(text):
    # This reaches out to macOS's built-in 'pbcopy' tool to save text to your clipboard
    process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, close_fds=True)
    process.communicate(input=text.encode('utf-8'))

print("\n==================================")
print("Terminal Password Generator (Smarter Version)")
print("==================================")

try:
    length = int(input("Enter desired password length (minimum 8): "))
    if length < 8:
        print("For security, length must be at least 8 characters. Setting to 8.")
        length = 8
        
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_characters) for _ in range(length))
    
    # Send the new password straight to your Mac clipboard!
    copy_to_clipboard(password)
    
    print("\n🔒 Your secure password has been generated:")
    print(f"👉  {password}")
    print("📋 [Copied directly to your clipboard! Just press Command+V to paste it anywhere].\n")

except ValueError:
    print("Invalid input! Please enter a valid number next time.")

