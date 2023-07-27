#El asterisco es cuando quieres mandar muchos valores en el argumento
def argumento(*num):
    for i in num:
        print(i)

print(argumento(10, 20 , 30 , 40 ,50))