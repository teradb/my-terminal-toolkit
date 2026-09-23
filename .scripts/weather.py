import urllib.request

print("\n==================================")
print("Welcome to your Terminal Weather Station!")
print("==================================")

city = input("Enter a city name: ").strip().replace(" ", "-")

if not city:
  print("City name cannot be blank!")
else:
  url = f"https://wttr.in{city}?0"
  try:
    print("\nFetching live weather data...\n")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
      html = response.read().decode('utf-8')
      print(html)
  except Exception as e:
    print("Oops! Could not retrieve weather data right now. The server might be down!")

