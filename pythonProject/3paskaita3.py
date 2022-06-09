import datetime
strftime(format)
ivesta_data = input("Įveskite norima datą ir laika: ")
data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
skirtumas = (datetime.datetime.now() - data)
print("kiek praejo metu: ", round(skirtumas.days // 365))
print("kiek praejo menesiu: ", round(skirtumas.days // 12))
print("kiek praejo dienu: ", skirtumas.days)
print("kiek praejo valandu: ",
print("kiek praejo minuciu: "
print("kiek praejo sekundziu: " round(total_seconds)




