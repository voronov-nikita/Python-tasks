# Решение
# Решение является, возможно, самым адаптивным
ls=[]
with open("name.csv", "r") as file:
    for i in file:
        for g in i.split(";"):
            if g.isalpha():
                ls.append(g)

print(len(ls) - len(set(ls)))


