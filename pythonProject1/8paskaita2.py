sarasas = list(range(51))
naujas = [x*10 for x in sarasas]
print(naujas)

sarasas = list(range(51))
dalinasi_is_7 = [x for x in sarasas if x % 7 == 0]
print(dalinasi_is_7)

pakelti_kvadratu = [x ** 2 for x in sarasas]
print(pakelti_kvadratu)

print(sum(pakelti_kvadratu))
print(min(pakelti_kvadratu))
print(max(pakelti_kvadratu))
print(mean(pakelti_kvadratu))
print(median(pakelti_kvadratu))

atbulai = sorted(pakelti_kvadratu, reverse=True)
print(atbulai)




