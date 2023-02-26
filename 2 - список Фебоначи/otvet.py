list_febon = [1, 1]

index_input = int(input())
for i in range(index_input-2+1):
    list_febon.append(sum(list_febon))
    del list_febon[0]

print(list_febon)
