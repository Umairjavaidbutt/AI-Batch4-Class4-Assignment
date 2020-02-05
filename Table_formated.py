# Print tables from 5 to 10 in cloumns
num_1 = int(input("Enter table from: "))
num_2 = int(input("Enter table to +1: "))


for x in range(1,11):
    print()
    for table in range(num_1, num_2):
        print(('{} * {} = {}'.format(x, table, x*table)), end = "\t")