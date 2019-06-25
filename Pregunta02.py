# ¿Qué es una historia de usuario?
# Una historia de usuario son especificaciónes sobre el proyecto (programa) 
# que hace el usuario o cliente para realizar
# 
# ¿Para que sirve?
# Las histrias de usuario sirven para cumplir con las necesidades del cliente o usuario 
# 
# Ejemplo de uso: E
# Clinetes de la "Tambo"
# Asunto : Como anunciar al ganador de una promoción
# °El cliente debe ser llamado por su nombre.
# °Si el cliente tiene mas de 10 tickets debe ganar la promoción. 
#  debe de salir la frase "Gracias por su compra. Ganaste la nueva promocion"
# °Si el cliente no tiene mas de 10 ticket debe salir 
#  el mensaje "Agradecemos su compra pero debe de juntar todos los tickets pedidos"
# °Ademas debe decir el numero de tickets que se tiene



Cliente = input("Ingrese su nombre: ")
Tickets = int(input("Ingrese numnero de tickets: "))
if 0 < Tickets >= 5:
    print (Cliente, "Gracias por su compra. Ganaste la nueva promocion. Tu numero de tickets es: ", Tickets)
else :
    print (Cliente, "Agradecemos su compra pero debe de juntar todos los tickets pedidos." 
            ,"Tu numero de tickets es: ", Tickets)