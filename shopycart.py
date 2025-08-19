cart=[]
print("Welcome to the shopping cart!")
print("1. Add item\n","2. Remove item\n","3. Update items\n","4. View items\n","5. Search items\n","6. Slice Cart\n","7. Sort Cart\n","8. Exit\n")

while True:
    
    print("Enter your choice: ")
    n = int(input())
    if n==1:
        item=input("Enter item to add: ")
        cart.append(item)

    elif n==2:
        r = int(input("Enter index of item to remove: "))
        cart.pop(r)

    elif n==3:
        item = input("Enter item to update;")
        item2 = input("Enter new item:")
        cart[item]=item2
        

    elif n==4:
        
        print(cart)

    elif n==5:
        item = input("Enter item you needed;")
        print(cart.index(item))
        sv = input("enter search item:")
        i=0
        while(len(cart)):
            if (sv==cart[i]):
                print("Item found at index:", i)
                break
            else:
                i=i+1
                print("Item not found")
    elif n==6:
        print("\nSlicing...")
        start=int(input("Enter start index: "))
        end=int(input("Enter end index: "))
        print(cart[start:end])

    elif n==7:
        cart.sort()
        print(cart)

    else:
       print("Your session is over.. Thanku")
       exit()

        