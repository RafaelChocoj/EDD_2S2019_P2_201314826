
import curses #import the curses library
import hashlib #para hash

import time
from Carga_Data import Import_data #para importar datos en csv

from ListaDoble import ListaDob #para lista de bloques
lis_blocks = ListaDob()

from carga_json import Import_json #para leer el jeson vr freddy actual
#jason_read = Import_json()

global node_block_ac #para el bloque actual seleccionado
node_block_ac = None

from Arbol_AVL import arbol_AVL #para el arbol avl
tree_avl = arbol_AVL()

from Data_Espera import Data_wating
data_en_espera = Data_wating()

import threading

#########para cliente
import socket
import select
import sys

"""
#para verificar si se escribio los parametros
if len(sys.argv) != 3:
    print ("error al ingresar parametros")
    print("Correct usage: script, IP address, port number")
    exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
"""

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
    #paint_menu(window)
    window.addstr(4,21, '*Bloque insertado')     
    size_bloques = data_en_espera.index
    date_now_str = data_en_espera.timestamp
    class_b = data_en_espera.class_b
    data = data_en_espera.data
    previous_hash = data_en_espera.previous_hash
    hash = data_en_espera.hash_b

    lis_blocks.Insert_fin(date_now_str,class_b, data, previous_hash, hash, size_bloques)

    #window.timeout(-1)  

def no_insert():
    #print("No insert")
    #paint_menu(window)
    window.addstr(4,21, 'Bloque no insertado')     
    window.addstr(5,21, 'Bloque hackeado :v')    
    data_en_espera.index = 0
    data_en_espera.timestamp = None
    data_en_espera.class_b = None
    data_en_espera.data = None
    data_en_espera.previous_hash = None
    data_en_espera.hash_b = None

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
    print("verificando")
    #paint_menu(window)
    window.addstr(2,21, 'verificando')  
    #server.sendall('true'.encode('utf-8'))
    #window.addstr(8,21, 'true, correcto')
    Es_correcto = is_jason(json_string)
    #print("Es_correcto "  + str(Es_correcto))
    
    if Es_correcto == True:
        data_json = json.loads(json_string)
        
        data_en_espera.index = data_json['INDEX']
        data_en_espera.timestamp = data_json['TIMESTAMP']
        data_en_espera.class_b = data_json['CLASS']

        json_dat = data_json['DATA']
        json_dat = json.dumps(json_dat)
        data_en_espera.data = json_dat

        data_en_espera.previous_hash = data_json['PREVIOUSHASH']
        data_en_espera.hash_b = data_json['HASH']

        #print(data_en_espera.index)
        #print(data_en_espera.class_b)

        ###creando el hast para ver si es el mismo
        #hash previo
        previous_hash = data_en_espera.previous_hash
        """
        size_bloques = data_en_espera.index
        #hash actual recibido
        
        hash_new = str(size_bloques) + data_en_espera.timestamp + data_en_espera.class_b + data_en_espera.data + previous_hash
        #hash_new = str(size_bloques)
        hash = hashlib.sha256(hash_new.encode())
        hash = hash.hexdigest()
        """

        ultimo_hash = lis_blocks.prev_hash()

        print("hash de prev jason:  " + previous_hash)
        print("hash de ultim aqui:  " + ultimo_hash)

        
        ###validando has recibido y hash aqui
        #if data_en_espera.hash_b == hash:
        if previous_hash == ultimo_hash:
            window.addstr(15,21, str(Es_correcto) +', correcto')
            window.addstr(16,21, 'hash correctos')
            #print('hash correctos')
            server.sendall('true'.encode('utf-8'))
        else:
            window.addstr(15,21, ' incorrecto')
            window.addstr(16,21, 'hash incorrectos')
            #print('hash incorrectos')
            server.sendall('false'.encode('utf-8'))


        #window.addstr(10,21, str(Es_correcto) +' true, correcto')
        #server.sendall('true'.encode('utf-8'))
    else:
        window.addstr(11,21, str(Es_correcto) +' false, no es json')
        server.sendall('false'.encode('utf-8'))


    """
       
    data_en_espera.index = 0
    data_en_espera.timestamp = None
    data_en_espera.class_b = None
    data_en_espera.data = None
    data_en_espera.previous_hash = None
    data_en_espera.hash_b = None
    """

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
                #if recibido == 'true':
                if recibido == 'true' or recibido == "true":
                    #paint_title(win,'respuesta de') 
                    insertando_nod()

                    #tecla = window.getch()  #####
                    window.getch()  #####
                #elif recibido == 'false':
                elif recibido == 'false' or recibido == "false":
                    no_insert()

                    window.getch()  #####
                    tecla = window.getch()  #####
                elif recibido == 'Welcome to [EDD]Blockchain Project!':
                    #print("no hacer nada")
                    nada = ""
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
        
def paint_recibidos(win, recib):
    paint_title(win,' Recibido ')          
    win.addstr(7,21, recib)             
    #win.addstr(8,21, '2. Select Block')       
    #win.addstr(9,21, '3. Reports')    
    #win.addstr(13,21, '7. Exit')            
    #win.timeout(-1)   


"""
#####
from CircularDoble import ListaCir #para lista cicrular del usuario
lis_user = ListaCir()
#####
from FilaPuntuaciones import FilaPuntos
tabla_puntos = FilaPuntos()

import Jugando_n_class

#global usuario_actual_play
usuario_actual_play = None
"""

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

data_im = Import_data()


def paint_menu(win):
    paint_title(win,' MAIN MENU ')          
    win.addstr(7,21, '1. Insert Block')             
    win.addstr(8,21, '2. Select Block')       
    win.addstr(9,21, '3. Reports')  
    #win.addstr(10,21, '4. Reports')         
    #win.addstr(11,21, '5. Bulk Loading')    
    win.addstr(13,21, '7. Exit')            
    #win.addstr(12,21, '6. New Player')    
    win.timeout(-1)                         

def paint_title(win,var):
    win.clear()                         
    win.border(0)                  
    x_start = round((60-len(var))/2)    
    win.addstr(0,x_start,var)   

    if node_block_ac != None:   
        nod_selct = node_block_ac.class_b
        x_start2 = round(58-len(nod_selct))    
        win.addstr(0,x_start2,nod_selct)         

def wait_esc(win):
    key = window.getch()
    while key!=27:
        key = window.getch()

def paint_reports(win):
    paint_title(win,' REPORTS ')         
    win.addstr(7,21, '1. BLOCKCHAIN REPORT')            
    win.addstr(8,21, '2. TREE REPORTS')        
   
    win.addstr(12,21, '(ESC). Salir')            
    #win.timeout(-1)    

def paint_reports_tree_rep(win):
    paint_title(win,' TREE REPORTS REPORTS ')         
    win.addstr(7,21, '1. Visualizar árbol')            
    win.addstr(8,21, '2. Mostrar recorridos')
    win.addstr(9,21, '3. Mostrar recorridos (Consola)')    

    win.addstr(12,21, '(ESC). Salir')            
  
def paint_reports_recorridos(win):
    paint_title(win,' RECORRIDO REPORTS ')         
    win.addstr(7,21, '1. Preorden')            
    win.addstr(8,21, '2. Posorden')  
    win.addstr(9,21, '3. Inorden')   

    win.addstr(12,21, '(ESC). Salir')

def paint_reports_recorridos_consola(win):
    paint_title(win,' RECORRIDO REPORTS CONSOLA ')         
    win.addstr(7,21, '1. Preorden (consola)')            
    win.addstr(8,21, '2. Posorden (consola)')  
    win.addstr(9,21, '3. Inorden (consola)')   

    win.addstr(12,21, '(ESC). Salir')

"""

def paint_tablapuntos(win):
    paint_title(win,' 2 - SCOREBOARD ')         
    win.addstr(3,18, 'NAME')     
    win.addstr(3,41, 'SCORE')  
    y_nam = 4      
    print_score = tabla_puntos.primero_head
    while print_score != None:            
        #print( print_score.name + " - " + str(print_score.puntos )  )
        win.addstr(y_nam,18, str(print_score.name)) 
        win.addstr(y_nam,41, str(print_score.puntos ))           
        print_score = print_score.siguiente
        y_nam = y_nam +1

    #win.addstr(4,18, '1. Score Report')      
    #win.addstr(5,18, '2. Scoreboard Report')  
    #win.addstr(6,18, '3. Users Report')  
    #win.addstr(7,18, '4. Users Report')  
    #win.addstr(8,18, '5. Users Report')  
    #win.addstr(9,18, '6. Users Report')  
    #win.addstr(10,18, '7. Users Report')
    #win.addstr(11,18, '8. Users Report')
    #win.addstr(12,18, '9. Users Report')  
    #win.addstr(13,18, '10. Users Report')        
    win.addstr(16,21, '(ESC). Salir')      
               
def scoreboard(win):
    
    while True:
        paint_tablapuntos(win)
        tecla = window.getch()
        if tecla == 27:
            break

"""
#para reporte de recorrido del arbol
def report_select_recorrido(win):
     
    while True:
        paint_reports_recorridos(win)
        tecla = window.getch()
        
        if tecla == 49: #1  Preorden
            #Jugando_n_class.game_graf_serpiente()
            tree_avl.Graficando_preor()
            #break
        elif tecla == 50: #2  Posorden
            tree_avl.Graficando_posor()
        elif tecla == 51: #3  Inorden
            tree_avl.Graficando_inor()
        elif tecla == 27:
            break

def paint_recorr_consola(win, recor_str):         
    y = 4
    x = 5
    #y =y+1
    hash_ac = str(recor_str)
    tem = ""
    for row in hash_ac:
        tem = tem + row
        if len(tem) > 50:
            win.addstr(y,x, tem )
            y =y+1
            tem = ""
    win.addstr(y,x, tem )

    win.addstr(12,21, '(ESC). Salir')

#para reporte de recorrido del arbol
def report_select_recorrido_consola(win):
     
    while True:
        paint_reports_recorridos_consola(win)
        tecla = window.getch()
        
        if tecla == 49: #1  Preorden
            str_preor = tree_avl._preorder_con()
            #print(str_preor)
            paint_title(win,' PREORDER ') 
            vista_recorrido_consola(win, str_preor)
            #break
        elif tecla == 50: #2  Posorden

            str_posr = tree_avl._postorder_con()
            #print(str_posr)
            paint_title(win,' POSORDER ') 
            vista_recorrido_consola(win, str_posr)


        elif tecla == 51: #3  Inorden
            str_inor = tree_avl._inorder_con()
            #print(str_inor)
            paint_title(win,' INORDER ') 
            vista_recorrido_consola(win, str_inor)
        elif tecla == 27:
            break

#para reporte de recorrido del arbol
def vista_recorrido_consola(win, str_preor):
    while True:
        paint_recorr_consola(win, str_preor)
        tecla = window.getch()
        
        if tecla == 27:#escape
            break

#para reporte de Arbol
def report_select_arbol(win):
     
    while True:
        paint_reports_tree_rep(win)
        tecla = window.getch()
        
        if tecla == 49: #1
            #Jugando_n_class.game_graf_serpiente()
            tree_avl.Graficando_arbol()
            #break
        elif tecla == 50: #2
            report_select_recorrido(win)
        elif tecla == 51: #3
            report_select_recorrido_consola(win)
        elif tecla == 27:
            break

#para seleccionar reportes
def report_seleccion(win):
     
    while True:
        paint_reports(win)
        tecla = window.getch()
        
        if tecla == 49: #1
            lis_blocks.graf_blockchain()
            #break
        elif tecla == 50: #2
            #Jugando_n_class.game_graf_score()
            report_select_arbol(win)


        elif tecla == 27:
            break

"""
 #empezar a jugar
def play_snake_now(win):   
    global usuario_actual_plays
    while True:
        paint_title(win," Presione Enter ")
            
        des = 'Aceptar'
        x_start = round((60-len(des))/2)
        win.addstr(8,x_start, des) 

        tecla = win.getch()

        if tecla == 10:
            #si el tipo de juego es 0, se tiene que reiniciar juego
            global tipo_de_juego
            ##import Jugando_n_class
            #Jugando_n_class.Obtener_jugador(usuario_actual_play)
            
            global dire
            #print("tipo_de_juego: " + str(tipo_de_juego))
            tipo_gg = Jugando_n_class.play_now(usuario_actual_play, tipo_de_juego, dire)
            tipo_de_juego = tipo_gg
            if (tipo_gg== 0):
                paint_title(win," Moriste Wee ")
                des = 'Game Over'
                x_start = round((60-len(des))/2)
                win.addstr(8,x_start,des) 
                #inserto punto y nombre
                pts =Jugando_n_class.get_puntos()
                tabla_puntos.insertNodo(usuario_actual_play, pts)   

                while True:
                    if win.getch() == 27:
                        break
            elif (tipo_gg== 1):
                paint_title(win," Presione Enter ")
                dire = Jugando_n_class.get_direction()
                #print("dire :" + str(dire))
                des = 'Pause'
                x_start = round((60-len(des))/2)
                win.addstr(8,x_start,des) 

                win.getch()
                break
            break
        elif tecla == 27:
            break

#empezar a jugar
def play_snake(win):
    tipo_gg = 0
    global usuario_actual_play
    if (usuario_actual_play == None):
        pintar_usuarios(win, "Ningun Jugador Seleccionado")  
        win.addstr(7,21, 'N. Nuevo Jugador')            
        while True:
            tecla = win.getch()
            if tecla == 110 or tecla == 78:
                paint_title(win," Nuevo Jugador ")
                win.addstr(3,21, 'Ingrese numbre de jugador')  

                win.keypad(False)    
                curses.echo()         
                curses.curs_set(1)     
                nombre_archivo  = win.getstr(6,20).decode(encoding="utf-8")

                usuario_actual_play = nombre_archivo
                data_im.new_user(usuario_actual_play)

                win.keypad(True)    
                curses.noecho()         
                curses.curs_set(0) 

                #play_snake(win)
                play_snake(win)
                tecla = 27
                break

            elif tecla == 27:
                break
    else:
          
        while True:
            paint_title(win," Presione Enter ")
               
            des = 'Aceptar'
            x_start = round((60-len(des))/2)
            win.addstr(8,x_start, des) 

            tecla = win.getch()

            if tecla == 10:
                #si el tipo de juego es 0, se tiene que reiniciar juego
                global tipo_de_juego
                ##import Jugando_n_class
                #Jugando_n_class.Obtener_jugador(usuario_actual_play)
                
                global dire
                #print("tipo_de_juego: " + str(tipo_de_juego))
                tipo_gg = Jugando_n_class.play_now(usuario_actual_play, tipo_de_juego, dire)
                tipo_de_juego = tipo_gg
                if (tipo_gg== 0):
                    paint_title(win," Moriste Wee ")
                    des = 'Game Over (NANI)'
                    x_start = round((60-len(des))/2)
                    win.addstr(8,x_start,des) 
                    #inserto punto y nombre
                    #pts =Jugando_n_class.get_puntos()
                    pts =Jugando_n_class.get_puntos_totales()
                    tabla_puntos.insertNodo(usuario_actual_play, pts)   

                    while True:
                        if win.getch() == 27:
                            Jugando_n_class.game_graf_serpiente()
                            break
                elif (tipo_gg== 1):
                    paint_title(win," Presione Enter ")
                    dire = Jugando_n_class.get_direction()
                    #print("dire :" + str(dire))
                    des = 'Pause'
                    x_start = round((60-len(des))/2)
                    win.addstr(8,x_start,des) 
 
                    win.getch()
                    break
                break
            elif tecla == 27:
                break

            #agregar nuevo jugador
            #elif tecla == 27:
            #    break
            
#empezar a jugar
def play_snake_back(win):
    tipo_gg = 0
    global usuario_actual_play
    if (usuario_actual_play == None):
        pintar_usuarios(win, "Ningun Jugador Seleccionado")  
        win.addstr(7,21, 'N. Nuevo Jugador')            
        while True:
            tecla = win.getch()
            if tecla == 110 or tecla == 78:
                paint_title(win," Nuevo Jugador ")
                win.addstr(3,21, 'Ingrese numbre de jugador')  

                win.keypad(False)    
                curses.echo()         
                curses.curs_set(1)     
                nombre_archivo  = win.getstr(6,20).decode(encoding="utf-8")

                usuario_actual_play = nombre_archivo
                data_im.new_user(usuario_actual_play)

                win.keypad(True)    
                curses.noecho()         
                curses.curs_set(0) 

                #play_snake(win)
                play_snake(win)
                tecla = 27
                break

            elif tecla == 27:
                break
    else: 
        
        
        while True:
            paint_title(win," Presione Enter ")
               
            des = 'Aceptar'
            x_start = round((60-len(des))/2)
            win.addstr(8,x_start, des) 

            tecla = win.getch()

            if tecla == 10:
                #si el tipo de juego es 0, se tiene que reiniciar juego
                global tipo_de_juego
                ##import Jugando_n_class
                #Jugando_n_class.Obtener_jugador(usuario_actual_play)
                
                global dire
                #print("tipo_de_juego: " + str(tipo_de_juego))
                tipo_gg = Jugando_n_class.play_now(usuario_actual_play, tipo_de_juego, dire)
                tipo_de_juego = tipo_gg
                if (tipo_gg== 0):
                    paint_title(win," Moriste Wee ")
                    des = 'Game Over (NANI)'
                    x_start = round((60-len(des))/2)
                    win.addstr(8,x_start,des) 
                    #inserto punto y nombre
                    #pts =Jugando_n_class.get_puntos()
                    pts =Jugando_n_class.get_puntos_totales()
                    tabla_puntos.insertNodo(usuario_actual_play, pts)   

                    while True:
                        if win.getch() == 27:
                            break
                elif (tipo_gg== 1):
                    paint_title(win," Presione Enter ")
                    dire = Jugando_n_class.get_direction()
                    #print("dire :" + str(dire))
                    des = 'Pause'
                    x_start = round((60-len(des))/2)
                    win.addstr(8,x_start,des) 
 
                    win.getch()
                    break
                break
            elif tecla == 27:
                break


"""          
import datetime
def obtengo_lis_bloques():
    #global lis_blocks
    #lis_blocks = data_im.retorno_users()
    #lis_blocks.insert_ejemplo()


    f_ahora = datetime.datetime.today()
    date_now_str = f_ahora.strftime('%d-%m-%y::%H:%M:%S')
    #insert_inicio(index, timestamp, class_b, data, previous_hash, hash_b):
    lis_blocks.Insert_fin(date_now_str,"estructuras", "jasson1", "5465","as",0)
    lis_blocks.Insert_fin(date_now_str,"comp1", "jasson2", "5465","as",0)
    lis_blocks.Insert_fin(date_now_str,"ipc1", "jasson3", "5465","as",0)
    
    lis_blocks.Insert_fin(date_now_str,"lenguajes", "jasson5", "5465","as",0)

def insert_node_blocke(class_b, data):

    f_ahora = datetime.datetime.today()
    date_now_str = f_ahora.strftime('%d-%m-%y-::%H:%M:%S')
    #insert_inicio(index, timestamp, class_b, data, previous_hash, hash_b):
    """
    pru = 'hola mundo'
    hash = hashlib.sha256(pru.encode())
    hash = hash.hexdigest()
    print(hash)
    """
    ##lis_blocks.Insert_fin(date_now_str,class_b, data, hash, hash)
    #lis_blocks.Insert_fin(date_now_str,class_b, data, "", "")
    ######data = 'prueba'

    #hash previo
    previous_hash = lis_blocks.prev_hash()
    #print(previous_hash)
    size_bloques = lis_blocks.size
    #print(size_bloques)
    #creando hash actual
    hash_new = str(size_bloques) + date_now_str + class_b + data + previous_hash
    #hash_new = str(size_bloques) 
    hash = hashlib.sha256(hash_new.encode())
    hash = hash.hexdigest()
    #print(hash)
    

    data_en_espera.index = size_bloques
    data_en_espera.timestamp = date_now_str
    data_en_espera.class_b = class_b
    data_en_espera.data = data
    data_en_espera.previous_hash = previous_hash
    data_en_espera.hash_b = hash

    #####lis_blocks.Insert_fin(date_now_str,class_b, data, previous_hash, hash, size_bloques)

    
    data_json = {}
    data_json['INDEX'] = size_bloques
    data_json['TIMESTAMP'] = date_now_str
    data_json['CLASS'] = class_b
    data_json['DATA'] = data
    data_json['PREVIOUSHASH'] = previous_hash
    data_json['HASH'] = hash

    json_send = json.dumps(data_json)
    
    #with open('prubb.json', 'w') as file:
    #    json.dump(data_json, file)

    data_json_str = "{ "
    data_json_str += "\"INDEX\": " + str(size_bloques) +","
    data_json_str += "\"TIMESTAMP\": \"" + date_now_str + "\","
    data_json_str += "\"CLASS\": \"" + class_b + "\","
    data_json_str += "\"DATA\": " + data + ","
    data_json_str += "\"PREVIOUSHASH\": \"" + previous_hash + "\","
    data_json_str += "\"HASH\": \"" + hash + "\""
    data_json_str += "} "

    #print ("<yo>")
    #print(json_send.encode())
    print(json_send)
    print(data_json_str)

    """
    with open('conlib.json', 'w') as file:
        json.dump(data_json, file)
    with open('sin_lib.json', 'w') as file:
        json.dump(data_json_str, file)
    f = open("sin_lib_op2.json", "w")

    f.write(data_json_str)
    f.close()
    """

    #server.sendall(json_send.encode())
    server.sendall(data_json_str.encode()) ##este es
   
    """

    server.sendall(json_send.encode())
    ########server.sendall("enviando desde insert node".encode('utf-8'))
    """

#para seleccionar usuarios
def block_seleccion(win):

    #para obtener lista de usuarios
    ############obtengo_lis_bloques()
    blocke_actual = lis_blocks.primero_head  

    dir_iz = ""
    dir_der = ""

    ##verificando si tiene usuarios ingresados
    if (blocke_actual == None):
        pintar_block(win, "No tiene bloques ingresados")
        while True:
            tecla = window.getch()
            if tecla == 27:
                break
    else:     
        block_name = blocke_actual.class_b

        block_name = block_name + " --->"
        dir_iz = ""
        dir_der = " --->"
        #pintar_block(win, block_name)
        pintar_block_f2(win, blocke_actual, dir_iz, dir_der)

        ##key_selec = window.getch()
        #print("00 pirn " + str(window.getch()))
        while True:
            #tecla = stdscr.getch()
            tecla = win.getch()
            if tecla == curses.KEY_RIGHT:

                if blocke_actual.siguiente != None:
                    blocke_actual = blocke_actual.siguiente

                    paint_title(window,' 2 - SELECT BLOCK ')
                    block_name = blocke_actual.class_b

                    if blocke_actual.siguiente != None:
                        block_name = "<--- " + block_name + " --->"
                        dir_iz = "<--- "
                        dir_der = " --->"
                    else:
                        block_name = "<--- " + block_name
                        dir_iz = "<--- "
                        dir_der = ""

                    #pintar_block(win, block_name)
                    pintar_block_f2(win, blocke_actual, dir_iz, dir_der)
        
            elif tecla == curses.KEY_LEFT:

                if blocke_actual.anterior != None:
                    blocke_actual = blocke_actual.anterior

                    paint_title(window,' 2 - SELECT BLOCK ')
                    block_name = blocke_actual.class_b

                    if blocke_actual.anterior != None:
                        block_name = "<--- " + block_name + " --->"
                        dir_iz = "<--- " 
                        dir_der = " --->"
                    else:
                        block_name = block_name + " --->"
                        dir_iz = ""
                        dir_der = " --->"
                    #pintar_block(win, block_name)
                    pintar_block_f2(win, blocke_actual,  dir_iz, dir_der)

            #si se preciona enter se selecciona el usuario
            elif tecla == 10:
                #global usuario_actual_play
                #usuario_actual_play = blocke_actual.class_b

                global node_block_ac
                node_block_ac = blocke_actual
                #solo para ejemplo
                #tree_avl.insert_ejemplo()

                jason_read = Import_json()
                jason_read.clean_tree()
                jason_read.read_json(node_block_ac.data)
                global tree_avl
                tree_avl = jason_read.retorno_tree()
                #tree_avl.Graficando_inor()

                break
            elif tecla == 27:
                break
            


def pintar_block(win, user):
    #stdscr.clear()
    #altura, ancho = stdscr.getmaxyx()
    #paint_title(window, ' USER SELECTION ')
    altura = 20 
    ancho = 60
    ######curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    y = int(altura/2)
    x = int(int(ancho/2) - (len(user)/2))
    #x = int(int(ancho/2) - (len(menu[index])/2))
    #stdscr.addstr(y,x, menu[index], curses.color_pair(2))
    #win.addstr(y,x, user, curses.color_pair(2))
    win.addstr(y,x, user )
    win.refresh()


def pintar_block_f2(win, blocke_actual, dir_iz, dir_der):
    #stdscr.clear()
    #altura, ancho = stdscr.getmaxyx()
    #paint_title(window, ' USER SELECTION ')
    altura = 20 
    ancho = 60
    ######curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    #y = int(altura/2)
    #x = int(int(ancho/2) - (len(user)/2))

    #y = 4
    y = 3
    x = 10

    #x = int(int(ancho/2) - (len(menu[index])/2))
    #stdscr.addstr(y,x, menu[index], curses.color_pair(2))
    #win.addstr(y,x, user, curses.color_pair(2))

    #win.addstr(y,x, user )

    win.addstr(y,x, "INDEX: " + str(blocke_actual.index))
    y =y+1
    win.addstr(y,x, "TIMESTAMP: " + blocke_actual.timestamp )
    y =y+1
    win.addstr(y,x, "CLASS: " + str(blocke_actual.class_b))
    y =y+1
    #######
    data_ac = str(blocke_actual.data )
    #data_ac =  "este \n una prueba \n"
    #data_ac = "12345678901234567890123456798"
    data_ac = data_ac.replace("\n", " ")
    win.addstr(y,x, "DATA: " + data_ac[0: 30])
    y =y+1
    win.addstr(y,x+3, data_ac[30: 60])
    y =y+1
    win.addstr(y,x+3, data_ac[60: 90])
    y =y+1
    #######

    #win.addstr(y,x, "PREVIOUSHASH: " + blocke_actual.previous_hash )
    #y =y+1
    win.addstr(y,x, "PREVIOUSHASH: ")
    y =y+1
    hash_ante = str(blocke_actual.previous_hash)
    #print(hash_ante)
    tem = ""
    for row in hash_ante:
        tem = tem + row

        if len(tem) > 31:
            win.addstr(y, x+3, tem )
            #win.addstr(y, x+24, tem )
            y =y+1
            tem = ""
    win.addstr(y,x+3, tem )
    y =y+1
    #win.addstr(y,x, "HASH: " + blocke_actual.hash_b )

    win.addstr(y,x, "HASH: ")
    y =y+1
    hash_ac = str(blocke_actual.hash_b)
    #win.addstr(y,x, "HASH: " + hash_ac )
    tem = ""
    for row in hash_ac:
        tem = tem + row

        if len(tem) > 31:
        #if len(tem) > 30:
            #win.addstr(y,x+ 16, tem )
            win.addstr(y,x+3, tem )
            y =y+1
            tem = ""
    win.addstr(y,x+3, tem )
    #y =y+1
    

    win.addstr(10,4, dir_iz)
    win.addstr(10,51, dir_der)

    win.refresh()

def import_archiv(win):

    while True:
        tecla = window.getch()
        if tecla == 115 or tecla == 83: #S
            paint_title(window,' 1 -  IMPORT ')
            win.addstr(4,15, 'Ingrese Nombre de Arhivo .csv') 

            #agregando texto para nombre csv#
            win.keypad(False)    
            curses.echo()         
            curses.curs_set(1)     
            #nombre_archivo  = win.getstr(6,20).decode(encoding="utf-8")
            nombre_archivo  = win.getstr(6,20).decode('utf-8')
            
            encontrad = False
            encontrad = data_im.importando(nombre_archivo)
            #print('encontrad: ' + str(encontrad))
            #print('nombre_archivo: *' + nombre_archivo +"*")
            paint_title(window,' 1 - IMPORT ')
            if (encontrad == True):
                #global lis_user
                #lis_user = data_im.retorno_users()
                window.addstr(8,5, '(Datos importados) Presione una tecla para salir')
                #print(data_im.retorno_class())
                print(data_im.retorno_data() )
                insert_node_blocke(data_im.retorno_class(), data_im.retorno_data()) ####para insertar para ejemplo
            elif (encontrad == False):
                window.addstr(8,5, 'Archivo no Encontrado')
                window.addstr(3,5, 'intente de nuevo') 
                #print('Archivo no Encontrado')

            win.keypad(True)    
            curses.noecho()         
            curses.curs_set(0) 

            tecla = window.getch()

            

            #window.timeout(-1)   
            break

        elif tecla == 110:
            break

        elif tecla == 27:
            break

"""
def new_player(win):

    if (tipo_de_juego == 0):            
        while True:
            pintar_usuarios(win, "Seleccione")  
            win.addstr(7,21, 'N. Nuevo Jugador')  
            tecla = win.getch()
            if tecla == 110 or tecla == 78:
                paint_title(win," Nuevo Jugador ")
                win.addstr(3,21, 'Ingrese numbre de jugador')  

                win.keypad(False)    
                curses.echo()         
                curses.curs_set(1)     
                nombre_archivo  = win.getstr(6,20).decode(encoding="utf-8")

                usuario_actual_play = nombre_archivo
                data_im.new_user(usuario_actual_play)

                global lis_user
                lis_user = data_im.retorno_users()

                win.keypad(True)    
                curses.noecho()         
                curses.curs_set(0) 

                tecla = 27
                break

            elif tecla == 27:
                break
    else:
        tecla = win.getch()
        pintar_usuarios(win, "No puede crear jugador")  
        win.addstr(7,21, 'hasta que termine el juego actual')    

   
def import_archiv_solo_prueba(win):
    sale = False
    key = window.getch()
    if (key == 27 or key == 110):
        sale = True
    if(key==115):
        paint_title(window,' 5 - BULK LOADING ')
        win.addstr(7,21, 'Importando Datos') 
        window.addstr(8,15, '(Datos importados) Presione una tecla para salir')  
        data_im.importando()
        #print("asdasdasdas")
        global lis_user
        lis_user = data_im.retorno_users()
        ##lis_user.Lista_imprimir_ade()
        #lis_user.graf_users()

        sale = False
    while (sale != True):
        key = window.getch()

        sale = True

"""

conectando()

stdscr = curses.initscr() #initialize console

#global window #### new para que sea global

window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

#conectando()

keystroke = -1
while(keystroke==-1):
    ##print("imprimeidno aglo")
    window.timeout(400) ############

    keystroke = window.getch()  #get current key being pressed
    
    if(keystroke==490): #1
        #import Jugando
        paint_title(window, ' PLAY (Batlle Royal)')
        #wait_esc(window)
        ####play_snake(window)
        paint_menu(window)
        keystroke=-1

    elif(keystroke==50): #2
        window.timeout(0)
        paint_title(window, ' SELECT BLOCK ')
        #wait_esc(window)
        block_seleccion(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51): #3
        window.timeout(0)
        paint_title(window, ' REPORTS ')
        #wait_esc(window)
        report_seleccion(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==49): #1
        window.timeout(-1)
        paint_title(window,' 1 INSERT BLOCK ')
        window.addstr(7,20, '¿Desea importar Archivo?')            
        window.addstr(8,30, 'S/N')  

        #print(window.getch())
        #if(window.getch() == 110):
        #    paint_menu(window)
        #wait_esc(window)
        import_archiv(window)
        window.timeout(-1)
        paint_menu(window)
        keystroke=-1

    #elif(keystroke==54):
    #    paint_title(window,' 6 NEW PLAYER ')
    #
    #    #wait_esc(window)
    #    new_player(window)
    #    paint_menu(window)
    #    keystroke=-1

    elif(keystroke==27):
        paint_menu(window)      #paint menu
        keystroke=-1
        
        

    elif(keystroke==55):
        #window.timeout(0)
        #print("user actual: " + usuario_actual_play)
        pass
    else:
        keystroke=-1
        #print(keystroke)

curses.endwin() #return terminal to previous state
