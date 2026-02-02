given_name = input()
names = set()
while given_name != "":
    if names.__contains__(given_name):
        print("Existing name")
        given_name = input()
    else:
        names.add(given_name)
        print("New name")
        given_name = input()
for name in names:
    print(name)