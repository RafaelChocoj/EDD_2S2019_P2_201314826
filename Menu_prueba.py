
import curses #import the curses library
import time
from Carga_Mas import Import_data #para importar datos en csv

#####
from CircularDoble import ListaCir #para lista cicrular del usuario
lis_user = ListaCir()
#####
from FilaPuntuaciones import FilaPuntos
tabla_puntos = FilaPuntos()

import Jugando_n_class

## usuario_actual_play
#global usuario_actual_play
usuario_actual_play = None
tipo_de_juego = 0
dire = 'KEY_RIGHT'

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN #import special KEYS from the curses library

data_im = Import_data()


def paint_menu(win):
    paint_title(win,' MAIN MENU ')          
    win.addstr(7,21, '1. Play (Battle Royale)')             
    win.addstr(8,21, '2. Scoreboard')       
    win.addstr(9,21, '3. User Selection')  
    win.addstr(10,21, '4. Reports')         
    win.addstr(11,21, '5. Bulk Loading')    
    win.addstr(13,21, '7. Exit')            
    win.addstr(12,21, '6. New Player')    
    win.timeout(-1)                         

def paint_title(win,var):
    win.clear()                         
    win.border(0)                      
    x_start = round((60-len(var))/2)    
    win.addstr(0,x_start,var)           

def wait_esc(win):
    key = window.getch()
    while key!=27:
        key = window.getch()

def paint_reports(win):
    paint_title(win,' REPORTS ')         
    win.addstr(7,21, '1. Snake Report')            
    win.addstr(8,21, '2. Score Report')      
    win.addstr(9,21, '3. Scoreboard Report')  
    win.addstr(10,21, '4. Users Report')        
    win.addstr(12,21, '(ESC). Salir')            
    #win.timeout(-1)    

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

#para seleccionar reportes
def report_seleccion(win):
     
    while True:
        paint_reports(win)
        tecla = window.getch()
        
        if tecla == 49: #1
            Jugando_n_class.game_graf_serpiente()
            #break
        elif tecla == 50: #2
            Jugando_n_class.game_graf_score()
        elif tecla == 51: #3
            tabla_puntos.graf_puntuaciones()
            #break
        elif tecla == 52: #4
            ## inicio verificando si tiene usuarios ingresados
            paint_title(win, '4. Users Report')
            user_actual = lis_user.primero_head
            if (user_actual == None):
                pintar_usuarios(win, "No tiene usuarios ingresados")
                while True:
                    tecla = window.getch()
                    if tecla == 27:
                        break
            else:
                lis_user.graf_users()

            ## fin verificando si tiene usuarios ingresados
        elif tecla == 27:
            break


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


            
def obtengo_lis_users():
    global lis_user
    lis_user = data_im.retorno_users()


#para seleccionar usuarios
def user_seleccion(win):

    #para obtener lista de usuarios
    obtengo_lis_users()
    user_actual = lis_user.primero_head  

    ##verificando si tiene usuarios ingresados
    if (user_actual == None):
        pintar_usuarios(win, "No tiene usuarios ingresados")
        while True:
            tecla = window.getch()
            if tecla == 27:
                break
    else:     
        user_name = user_actual.user
        user_name = "<--- " + user_name + " --->"
        pintar_usuarios(win, user_name)
        ##key_selec = window.getch()
        #print("00 pirn " + str(window.getch()))
        while True:
            #tecla = stdscr.getch()
            tecla = win.getch()
            if tecla == curses.KEY_RIGHT:
                user_actual = user_actual.siguiente

                paint_title(window,' 3 - USER SELECTION ')
                user_name = user_actual.user
                user_name = "<--- " + user_name + " --->"
                pintar_usuarios(win, user_name)
        
            elif tecla == curses.KEY_LEFT:
                user_actual = user_actual.anterior

                paint_title(window,' 3 - USER SELECTION ')
                user_name = user_actual.user
                user_name = "<--- " + user_name + " --->"
                pintar_usuarios(win, user_name)

            #si se preciona enter se selecciona el usuario
            elif tecla == 10:
                global usuario_actual_play
                usuario_actual_play = user_actual.user
                break
            elif tecla == 27:
                break
            
    

def pintar_usuarios(win, user):
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

def import_archiv(win):

    while True:
        tecla = window.getch()
        if tecla == 115 or tecla == 83: #S
            paint_title(window,' 5 - BULK LOADING ')
            win.addstr(4,15, 'Ingrese Nombre de Arhivo .csv') 

            #agregando texto para nombre csv#
            win.keypad(False)    
            curses.echo()         
            curses.curs_set(1)     
            nombre_archivo  = win.getstr(6,20).decode(encoding="utf-8")
            
            encontrad = False
            encontrad = data_im.importando(nombre_archivo)
            ##lis_user.Lista_imprimir_ade()
            #lis_user.graf_users()
            paint_title(window,' 5 - BULK LOADING ')
            if (encontrad == True):
                global lis_user
                lis_user = data_im.retorno_users()
                window.addstr(8,5, '(Datos importados) Presione una tecla para salir')
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



stdscr = curses.initscr() #initialize console
window = curses.newwin(20,60,0,0) #create a new curses window
window.keypad(True)     #enable Keypad mode
curses.noecho()         #prevent input from displaying in the screen
curses.curs_set(0)      #cursor invisible (0)
paint_menu(window)      #paint menu

keystroke = -1
while(keystroke==-1):
    keystroke = window.getch()  #get current key being pressed
    if(keystroke==49): #1
        #import Jugando
        paint_title(window, ' PLAY (Batlle Royal)')
        
        #wait_esc(window)
        play_snake(window)
        
        paint_menu(window)
        keystroke=-1
    elif(keystroke==50):
        paint_title(window, ' SCOREBOARD ')
        #wait_esc(window)
        scoreboard(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==51):
        paint_title(window, ' USER SELECTION ')
        #wait_esc(window)
        user_seleccion(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==52):
        paint_title(window, ' REPORTS ')
        #wait_esc(window)
        report_seleccion(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==53):
        paint_title(window,' 5 BULK LOADING ')
        window.addstr(7,21, '¿Desea importar Usuarios?')            
        window.addstr(8,21, 'S/N')  

        #print(window.getch())
        #if(window.getch() == 110):
        #    paint_menu(window)

        #wait_esc(window)
        import_archiv(window)
        paint_menu(window)
        keystroke=-1

    elif(keystroke==54):
        paint_title(window,' 6 NEW PLAYER ')

        #wait_esc(window)
        new_player(window)
        paint_menu(window)
        keystroke=-1
    elif(keystroke==55):
        #print("user actual: " + usuario_actual_play)
        pass
    else:
        keystroke=-1

curses.endwin() #return terminal to previous state
