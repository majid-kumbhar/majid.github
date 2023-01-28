bol=True
while bol==True:
    bol_2=True

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
    
    while bol_2==True:

        decission=input("\nIf you want to continue then typy yes :")
        if decission=="yes":
            decission="yes"
            bol=True
            bol_2=False
    
        elif decission=="no":
            print("\nHave A Good Day BYE :)")
            bol_2=False
            bol=False
        
        else :
            print("\nPlease Refill \"yes\" or \"no\" :)")
            bol_2==False