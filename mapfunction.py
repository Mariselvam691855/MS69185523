user  = [int(item) for item in input("Enter the list items using ,: ").split(",")]
print("Orginal List : ", user)
result = map(lambda x : x*3, user)
print("\nTriple of list number : ")
print(list(result))