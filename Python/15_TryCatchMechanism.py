
try:
    with open('ReadWrite.txt', 'r') as Book:
        Book.read()

except:
    print("No data found 🥴...")


try:
    with open('ReadWrite.txt', 'r') as Book:
        Book.read()

except Exception as e:
    print(e)
finally:
    print("Troubleshooting issue...")