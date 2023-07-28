while True:
    try:
       edad = int(input("Ingresa tu edad: "))
       print("Tu edad es: ",edad)
       break
    #except zeroDivisionError
    #except ValueError
    except KeyboardInterrupt:
        print("\nHas cancelado la ejecucion")
        break