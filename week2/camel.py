# TESTS
# convert input from camel to snake case
# name > name
# firstName > first_name
# preferrdFirstName > preferred_first_name

ans = input("camelCase: ")
print("snake_case ", end="")
#print the second line "snake"
#loop 
for a in ans:
    if a.isupper():
        
        """does not work if you use the
        variable name 'ans'
        instead of 'a', inthe loops
        veryfies the upper letters"""
        
        print("_" + a.lower(), end="")

    else:
        print(a, end="")

