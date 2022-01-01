#python program for determining odd and even Numbers
while 1==1: #to make our program run forever
    try:
        n=int((input("Enter Your Number: ")))
    except:
        print("Only integers allowed")
        exit()
    if n%2==0:
        print("It's Even")
    else:
        print("It's Odd")
    o=input("Wanna Check another Number? (Y/N): ")
    if o in ['N','n']:
        print("Okie, exiting")
        exit()