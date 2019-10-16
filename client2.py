import threading

#########para cliente
import socket
import select
import sys


def conectando():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #if len(sys.argv) != 3:
    #	print ("Correct usage: script, IP address, port number")
    #	exit()

    #print("entra aqui corriendo")

    #IP_address = str(sys.argv[1])
    #Port = int(sys.argv[2])
    IP_address = str("localhost")
    Port = int(8080)

    server.connect((IP_address, Port))


    run_cliente = threading.Thread(target=run_cliente_sockets)


    #run_cliente.daemon = True
    run_cliente.start()

def insertando_nod():
    print("insertado")
    #window.addstr(8,21, 'Bloque insertado')     
    #size_bloques = data_en_espera.index
    #date_now_str = data_en_espera.timestamp
    #class_b = data_en_espera.class_b
    #data = data_en_espera.data
    #previous_hash = data_en_espera.previous_hash
    #hash = data_en_espera.hash_b

    #lis_blocks.Insert_fin(date_now_str,class_b, data, previous_hash, hash, size_bloques)


def no_insert():
    print("No insert")
    #window.addstr(8,21, 'Bloque no insertado')     
    ##window.addstr(9,21, 'Bloque no hackeado :v')    
    #data_en_espera.index = 0
    #data_en_espera.timestamp = None
    #data_en_espera.class_b = None
    #data_en_espera.data = None
    #data_en_espera.previous_hash = None
    #data_en_espera.hash_b = None

import json
def is_jason(json_string):
    try:
        json.loads(json_string)
        return True
    #except ValueError as error:
    except ValueError:
        #print("invalid json: %s" % error)
        return False

def verificando_bloque_recibido(json_string):
    print("--verificando--")
    #window.addstr(8,21, 'verificando')  
    #server.sendall('true'.encode('utf-8'))
    #window.addstr(8,21, 'true, correcto')
    print("json_string::::: *" +  json_string+"*")
    """
    Es_correcto = is_jason(json_string)
    print("Es_correcto "  + str(Es_correcto))
    
    if Es_correcto == True:
        data_json = json.loads(json_string)
        print("class")
        print(data_json['CLASS'])


        #window.addstr(10,21, str(Es_correcto) +' true, correcto')
        server.sendall('true'.encode('utf-8'))
    else:
        #window.addstr(10,21, str(Es_correcto) +' false, no es jason')
        server.sendall('false'.encode('utf-8'))
    """
    if json_string == 'saber.csv':
        server.sendall('true'.encode('utf-8'))
    else:
        server.sendall('false'.encode('utf-8'))




def run_cliente_sockets():
    #print("entra aqui run_cliente_sockets")
    while True:

        read_sockets = select.select([server], [], [], 1)[0]
        import msvcrt
        if msvcrt.kbhit(): read_sockets.append(sys.stdin)

        #print ("antes del for")
        for socks in read_sockets:
            #print ("for: " + str(socks))
            if socks == server:
                message = socks.recv(2048)
                print ("<recibido>")
                recibido = message.decode('utf-8')
                print(recibido)
                if recibido == 'true':
                    insertando_nod()
                elif recibido == 'false':
                    no_insert()
                elif recibido == 'Welcome to [EDD]Blockchain Project!':
                    print("no hacer nada")
                else:
                    verificando_bloque_recibido(recibido)

                ##para recibir
                #report_seleccion(window)

                #############paint_recibidos(window, message.decode('utf-8'))

                #paint_menu(window)
            else:
                #message = sys.stdin.readline()
                #texto_a_enviar = message
                #server.sendall(texto_a_enviar.encode('utf-8'))
                #sys.stdout.write("<You>")
                #sys.stdout.write(message)
                sys.stdout.flush()
    server.close()

conectando()

def Menu_prin():
    men = True
    while(men):
        print("***********MENU***********")
        print("1. Insert csv")
        print("7. salir")
        print("**************************")
        print("Selecciona opcion:")
        opcion = input()
        print("op: " + opcion)
        if (opcion == "1"):
            archivo = input("ingrese archivo csv: ")
            print("archivo: " + archivo)
            server.sendall(archivo.encode())
        elif (opcion == "7"):
            men = False


Menu_prin()