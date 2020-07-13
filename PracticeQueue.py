from collections import deque

bank=deque(["Chandan","Abir","Akash"])
print(bank)
bank.popleft()

print(bank)
bank.popleft()

print(bank)
bank.popleft()

if  not bank:
    print("No person left")
