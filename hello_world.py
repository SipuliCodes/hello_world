from datetime import datetime

current_hour = datetime.now().hour

if 5 <= current_hour <= 10:
    print("Good morning, World!")
elif 10 < current_hour <= 12:
    print("Hello World!")
elif 12 < current_hour < 18:
    print("Good afternoon, World!")
elif 18 <= current_hour < 21.00:
    print("Good Evening, World!")
elif 21 <= current_hour <= 23:
    print("Good Night, World!")
else:
    print("You should be sleeping")
