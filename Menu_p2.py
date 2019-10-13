
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

    win.addstr(12,21, '(ESC). Salir')            
  
def paint_reports_recorridos(win):
    paint_title(win,' RECORRIDO REPORTS ')         
    win.addstr(7,21, '1. Preorden')            
    win.addstr(8,21, '2. Posorden')  
    win.addstr(9,21, '3. Inorden')   

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

        #elif tecla == 51: #3
        #    tabla_puntos.graf_puntuaciones()
        #    #break
        #elif tecla == 52: #4
        #    ## inicio verificando si tiene usuarios ingresados
        #    paint_title(win, '4. Users Report')
        #    user_actual = lis_user.primero_head
        #    if (user_actual == None):
        #        pintar_usuarios(win, "No tiene usuarios ingresados")
        #        while True:
        #            tecla = window.getch()
        #            if tecla == 27:
        #                break
        #    else:
        #        lis_user.graf_users()

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
    lis_blocks.Insert_fin(date_now_str,"estructuras", "jasson1", "5465","as")
    lis_blocks.Insert_fin(date_now_str,"comp1", "jasson2", "5465","as")
    lis_blocks.Insert_fin(date_now_str,"ipc1", "jasson3", "5465","as")
    
    lis_blocks.Insert_fin(date_now_str,"lenguajes", "jasson5", "5465","as")

def insert_node_blocke(class_b, data):

    f_ahora = datetime.datetime.today()
    date_now_str = f_ahora.strftime('%d-%m-%y::%H:%M:%S')
    #insert_inicio(index, timestamp, class_b, data, previous_hash, hash_b):
    """
    pru = 'hola mundo'
    hash = hashlib.sha256(pru.encode())
    hash = hash.hexdigest()
    print(hash)
    """
    #lis_blocks.Insert_fin(date_now_str,class_b, data, hash, hash)
    lis_blocks.Insert_fin(date_now_str,class_b, data, "", "")

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
            nombre_archivo  = win.getstr(6,20).decode(encoding="utf-8")
            
            encontrad = False
            encontrad = data_im.importando(nombre_archivo)
            paint_title(window,' 1 - IMPORT ')
            if (encontrad == True):
                #global lis_user
                #lis_user = data_im.retorno_users()
                window.addstr(8,5, '(Datos importados) Presione una tecla para salir')
                #print(data_im.retorno_class())
                #print(data_im.retorno_data() )
                insert_node_blocke(data_im.retorno_class(), data_im.retorno_data()) ####para insertar para ejemplo
            elif (encontrad == False):
                window.addstr(8,5, 'Archivo no Encontrado')

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

stdscr = curses.initscr() #initialize console
window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    
    if(keystroke==490): #1
        #import Jugando
        paint_title(window, ' PLAY (Batlle Royal)')
        #wait_esc(window)
        play_snake(window)
        paint_menu(window)
        keystroke=-1

    #elif(keystroke==500):
    #    paint_title(window, ' SCOREBOARD ')
    #    #wait_esc(window)
    #    scoreboard(window)
    #    paint_menu(window)
    #    keystroke=-1

    elif(keystroke==50): #2
        paint_title(window, ' SELECT BLOCK ')
        #wait_esc(window)
        block_seleccion(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51): #3
        paint_title(window, ' REPORTS ')
        #wait_esc(window)
        report_seleccion(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==49): #1
        paint_title(window,' 1 INSERT BLOCK ')
        window.addstr(7,20, '¿Desea importar Archivo?')            
        window.addstr(8,30, 'S/N')  

        #print(window.getch())
        #if(window.getch() == 110):
        #    paint_menu(window)
        #wait_esc(window)
        import_archiv(window)
        paint_menu(window)
        keystroke=-1

    #elif(keystroke==54):
    #    paint_title(window,' 6 NEW PLAYER ')
    #
    #    #wait_esc(window)
    #    new_player(window)
    #    paint_menu(window)
    #    keystroke=-1

    elif(keystroke==55):
        #print("user actual: " + usuario_actual_play)
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state
