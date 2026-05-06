initial_balance = int(input("Initial Balance: "))
n = int(input("Number of transactions: "))
requests = []

for _ in range(n):
    requests.append(int(input()))

for request in requests:
    if initial_balance < 0 or request % 100 != 0 or request > initial_balance:
        print("FALED")
    else:
        initial_balance -= request
        print("SUCESS")

print(initial_balance)    