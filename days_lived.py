from datetime import date

day1 = date.today()
day2 = date(2004,11,8)
diff = day1 - day2
print(f"You have lived",diff.days,"days")