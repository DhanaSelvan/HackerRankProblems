from collections import Counter
X = int(input())
shoe_size = map(int, input().split(" "))
Customer_no = int(input())
counter = dict(Counter(shoe_size))
size_list = counter.keys()
nos = counter.values()
final = []
for i in range(Customer_no):
    cust_size, amount = map(int, input().split(" "))
    if(cust_size in counter):
        available = counter[cust_size]
        if(counter[cust_size]!=0):

            final.append(amount)
            available = available-1
            counter.update({cust_size:available})
print(f"Sum = {sum(final)}")
    
        