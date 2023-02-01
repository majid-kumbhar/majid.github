while True:
    

    num_1=int(input("\nEnter any number :"))
    operator=str(input("\nEnter any operator : "))

    if operator=='/' or operator=="*" or operator=="-" or operator=="+":

        num_2=int(input("\nEnter any number :"))
    
        if operator == '+':
            result=num_1+num_2    

        elif operator == '-':
            result=num_1-num_2

        elif operator == '/':
            result=num_1/num_2

        elif operator == '*':
            result=num_1*num_2

        print("\n",num_1,operator,num_2,'=',result)

    else:

        print("\nInvalid operator try again ")
    
    while True:

        decission=input("\nIf you want to continue then typy yes or no to exit \nenter here :")
        if decission=="yes":
            break
    
        elif decission=="no":
            print("\nHave A Good Day BYE :)\n")
            exit()
        
        else :
            print("\nPlease Refill \"yes\" or \"no\" :)")