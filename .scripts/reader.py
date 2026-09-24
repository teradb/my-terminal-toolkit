import os

print("\n==================================")
print("Terminal Text File Reader & Analyzer")
print("==================================")

filename = input("Enter the file name or path to read (e.g., notes.txt): ").strip()

if not os.path.exists(filename):
    print(f"❌ Error: The file '{filename}' could not be found.")
elif os.path.isdir(filename):
    print(f"❌ Error: '{filename}' is a directory, not a file.")
else:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

            # Calculate basic statistics
            lines = content.splitlines()
            words = content.split()

            print("\n📊 --- FILE METRICS ---")
            print(f"Lines: {len(lines)} | Words: {len(words)} | Characters: {len(content)}")
            print("------------------------\n")

            print("📄 --- FILE CONTENTS ---")
            print(content)
            print("------------------------\n")
    except Exception as e:
        print(f"❌ Error reading file: {e}")


