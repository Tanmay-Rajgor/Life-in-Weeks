age = input("Enter your current age : ")

years = 90 - int(age)
days = round(years * 365)
weeks = round(years * 52)
months = round(years * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left in your life if you live till 90 years.")