
s = "FridaysSaturdaysSundaysSaydays"
num = s.count("s")
days = s[:-1].split("s")
print("There are", num, "fun days in a week")
mess = days[0]
print("Two of them are", mess, days[-1])

result = ""
for i in range(len(mess)):
        if i > 2:
            result = result + mess[i]
print("My favorite", result, "is Saturday.")