
class NodeDo:
    def __init__(self, index = None, timestamp = None, class_b = None, data = None, previous_hash = None, hash_b = None ):    
        #self.valor = valor
        #self.x_pos = x_pos    
        #self.y_pos = y_pos    

        self.index = index 
        self.timestamp = timestamp
        self.class_b = class_b 
        self.data = data 
        self.previous_hash = previous_hash 
        self.hash_b = hash_b

        self.siguiente = None       
        self.anterior =  None   

import os
import datetime
import hashlib #para hash

class ListaDob:
    def __init__(self):        
        self.primero_head = None 
        self.size = 0
        #self.ultimo = None

    def esVacio(self):
        return self.primero_head is None

    #para insertar nodo al principio
    #def insert_inicio(self, index, timestamp, class_b, data, previous_hash, hash_b):
    def insert_inicio(self, timestamp, class_b, data, previous_hash, hash_b):
    
        #new_nod = NodeDo(index, timestamp, class_b, data, previous_hash, hash_b)

        previous_hash = self.prev_hash()
        #print(previous_hash)

        ###creando hash actual
        hash_new = str(self.size) + timestamp + class_b + data + previous_hash
        #print(hash_new)
        hash = hashlib.sha256(hash_new.encode())
        hash = hash.hexdigest()
        #print(hash)

        new_nod = NodeDo(self.size, timestamp, class_b, data, previous_hash, hash)
        if self.esVacio():    
            self.primero_head = new_nod
            #self.ultimo = new_nod
        else:
            #new_nod.siguiente  = self.primero_head
            tempo = self.primero_head
            new_nod.siguiente  = tempo

            self.primero_head = new_nod
            tempo.anterior = new_nod

        self.size = self.size + 1


    #para obtener el hash anterior
    def prev_hash(self):
        if self.esVacio():
            hash_ante = "0000"
            return hash_ante
        else:
            
            tempo = self.primero_head
            while (tempo.siguiente is not None):
                tempo = tempo.siguiente
            hash_ante = tempo.hash_b
            return hash_ante

    #para insertar nodo Al final
    #def Insert_fin(self, index, timestamp, class_b, data, previous_hash, hash_b):
    def Insert_fin(self,  timestamp, class_b, data, previous_hash, hash_b, size_bloques):
        #new_nod = NodeDo(index, timestamp, class_b, data, previous_hash, hash_b)

        """
        previous_hash = self.prev_hash()
        #print(previous_hash)
        ###creando hash actual
        hash_new = str(self.size) + timestamp + class_b + data + previous_hash
        #print(hash_new)
        hash = hashlib.sha256(hash_new.encode())
        hash = hash.hexdigest()
        #print(hash)
        """

        hash = hash_b

        #new_nod = NodeDo(self.size, timestamp, class_b, data, previous_hash, hash)
        new_nod = NodeDo(size_bloques, timestamp, class_b, data, previous_hash, hash)


        if self.esVacio():
            self.primero_head = new_nod
            #self.ultimo = new_nod
        else:
            tempo = self.primero_head
            while (tempo.siguiente is not None):
                tempo = tempo.siguiente
            tempo.siguiente = new_nod
            new_nod.anterior = tempo
        self.size = self.size + 1

    #para eliminar nodo al principio
    def delete_inicio(self):

        if self.esVacio() == False:    
            ##esta vacia
            #print ("vacio")
        #else:
            aux = self.primero_head
            self.primero_head = self.primero_head.siguiente
            aux.siguiente = None
            self.primero_head.anterior = None
            #print ("eliminado")

        self.size = self.size - 1

    #para eliminar nodo al FINAL
    def delete_fin(self):

        if self.esVacio() == False:    
            ##esta vacia
            #print ("vacio")
        #else:
            #aux = self.primero_head
            #self.primero_head = self.primero_head.siguiente
            #aux.siguiente = None
            #self.primero_head.anterior = None

            temp_prin = self.primero_head
            while temp_prin.siguiente is not None: 
            #while temp_prin != None: 
                tempo = temp_prin 
                temp_prin = temp_prin.siguiente                     

            tempo.siguiente = None
            temp_prin.anterior = None
            
            ##print ("eliminado")


        self.size = self.size - 1

            
    #Imprimir lista adelante
    def Lista_imprimir_ade(self):
    #def Lista_imprimir_ade():
        if self.esVacio():
            print ("La  lista esta vacia")
        else:
            temp_prin = self.primero_head
            #while temp_prin.siguiente is not None:        
            #    #print( temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )   
            #    print(str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )             
            #    temp_prin = temp_prin.siguiente
            ##print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) ) 
            #print(str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) ) 

            while temp_prin != None:         
                print(str(temp_prin.index) + " - "+ str(temp_prin.class_b) + " - "+ str(temp_prin.timestamp))             
                temp_prin = temp_prin.siguiente

    #Imprimir lista atras
    def Lista_imprimir_atra(self):
        if self.esVacio():
            print ("La  lista esta vacia")
        else:

            temp_prin = self.primero_head
            while temp_prin.siguiente is not None:  
                temp_prin = temp_prin.siguiente      
            while temp_prin.anterior is not None: 
                #print(str(temp_prin.index) + " - " + str(temp_prin.class_b) + ","+ str(temp_prin.data) ) 
                print(str(temp_prin.index) + " - " + str(temp_prin.class_b)) 
                temp_prin = temp_prin.anterior
            print(str(temp_prin.index) + " - " + str(temp_prin.class_b)) 

    #para graficar en grapiz
    def graf_serpiente_solo_prueba(self):

        f = open("list_ser.txt", "w")

        #f.write("digraph G {\n")
        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")
        #f.write("node [shape = square];\n")

        #l = ["A1", "B2","C3","D4","E5", "F6"]
        #for i in range(len(l)-1):
        #    f.write("\""+ l[i]+ "\"->\"JUAN\";\n")
        temp_prin = self.primero_head
        #while temp_prin.siguiente is not None:    
        while temp_prin != None:    
            #print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) )  
            nodo_name = str(temp_prin.x_pos) + str(temp_prin.y_pos)
            nodo_corde = "(" + str(temp_prin.x_pos) + "," + str(temp_prin.y_pos) + ")"
            f.write("node"+ nodo_name +"[label = \"{<f0>|<f1> "+ nodo_corde +"|<f2> }\"];\n")  
            
            if (temp_prin.anterior == None):
                f.write("node_n1[label = \"null\"];\n")  
                f.write("node"+ nodo_name +":f0 -> node_n1;\n" )           
            
            f.write("node"+ nodo_name +"-> ")

            #if (temp_prin == self.primero_head):
            #    f.write("node"+ nodo_name +"-> NULL1;\n")

            temp_prin = temp_prin.siguiente

            if (temp_prin != None):
                #nodo_name_sig = "-"
                #########
                nodo_name_sig = str(temp_prin.x_pos) + str(temp_prin.y_pos)
                f.write("node"+ nodo_name_sig +";\n")

                #regreoso
                f.write("node"+ nodo_name_sig +"-> node" + nodo_name+";\n")
                #node0 -> node1;
            else:
                f.write("node_n2;\n")  
                f.write("node_n2[label = \"null\"];\n")   

        #print(temp_prin.valor + " - " + str(temp_prin.x_pos) + ","+ str(temp_prin.y_pos) ) 

        f.write("}")
        f.close()

        os.system("dot -Tpng list_ser.txt -o list_ser.jpg")
        #os.system("list_ser.txt")
        os.system("list_ser.jpg")
        #print("f en el chat")

        #para graficar en grapiz
    
    def graf_serpiente(self):

        f = open("list_ser.txt", "w")

        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape=record];\n")

        temp_prin = self.primero_head
        #while temp_prin.siguiente is not None:    
        nod_con = 0
        while temp_prin != None:    
            #nodo_name = str(temp_prin.x_pos) + str(temp_prin.y_pos)
            nodo_name = str(nod_con)
            nodo_corde = "(" + str(temp_prin.x_pos) + "," + str(temp_prin.y_pos) + ")"
            f.write("node"+ nodo_name +"[label = \"{<f0>|<f1> "+ nodo_corde +"|<f2> }\"];\n")  
            
            if (temp_prin.anterior == None):
                f.write("node_n1[label = \"null\"];\n")  
                f.write("node"+ nodo_name +":f0 -> node_n1;\n" )           
            
            f.write("node"+ nodo_name +"-> ")


            temp_prin = temp_prin.siguiente
            nod_con = nod_con +1

            if (temp_prin != None):
                #odo_name_sig = str(temp_prin.x_pos) + str(temp_prin.y_pos)
                nodo_name_sig = str(nod_con)
                #nodo_name_ante = str(temp_prin.anterior.x_pos ) + str(temp_prin.anterior.y_pos)
                nodo_name_ante = str(nod_con - 1)
                f.write("node"+ nodo_name_sig +";\n")

                #regreoso
                #f.write("node"+ nodo_name_sig +"-> node" + nodo_name+";\n")
                f.write("node"+ nodo_name_sig +"-> node" + nodo_name_ante+";\n")

            else:
                f.write("node_n2;\n")  
                f.write("node_n2[label = \"null\"];\n")   

        f.write("}")
        f.close()

        os.system("dot -Tpng list_ser.txt -o list_ser.jpg")
        #os.system("list_ser.txt")
        os.system("list_ser.jpg")


    def graf_blockchain(self):

        f = open("list_block.txt", "w")

        f.write("digraph G { rankdir=TB\n")
        f.write("node [shape=record];\n")

        temp_prin = self.primero_head
        #while temp_prin.siguiente is not None:    
        nod_con = 0
        while temp_prin != None:    
            nodo_name = str(nod_con)
            blockchain = "Class = " + temp_prin.class_b + "\\n" 
            blockchain = blockchain + "TimeStamp = " + temp_prin.timestamp + "\\n" 
            blockchain = blockchain + "PSHASH = " + temp_prin.previous_hash + "\\n" 
            blockchain = blockchain + "HASH = " + temp_prin.hash_b  
  
            f.write("node"+ nodo_name +"[label = \"{<f0>|<f1> "+ blockchain +"|<f2> }\"];\n")  
            
            if (temp_prin.siguiente != None):
                f.write("node"+ nodo_name +"-> ")


            temp_prin = temp_prin.siguiente
            nod_con = nod_con +1

            if (temp_prin != None):
                #odo_name_sig = str(temp_prin.x_pos) + str(temp_prin.y_pos)
                nodo_name_sig = str(nod_con)
                #nodo_name_ante = str(temp_prin.anterior.x_pos ) + str(temp_prin.anterior.y_pos)
                nodo_name_ante = str(nod_con - 1)
                f.write("node"+ nodo_name_sig +";\n")

                #regreoso
                f.write("node"+ nodo_name_sig +"-> node" + nodo_name_ante+";\n")


        f.write("}")
        f.close()

        os.system("dot -Tpng list_block.txt -o list_block.jpg")
        os.system("list_block.jpg")

    def insert_ejemplo(self):
        lis_dob = ListaDob()
        f_ahora = datetime.datetime.today()
        date_now_str = f_ahora.strftime('%d-%m-%y::%H:%M:%S')
        #insert_inicio(index, timestamp, class_b, data, previous_hash, hash_b):
        lis_dob.Insert_fin(date_now_str,"estructuras", "jasson1", "5465","as")
        lis_dob.Insert_fin(date_now_str,"comp1", "jasson2", "5465","as")
        lis_dob.Insert_fin(date_now_str,"ipc1", "jasson3", "5465","as")
        
        lis_dob.Insert_fin(date_now_str,"lenguajes", "jasson5", "5465","as")

        lis_dob.graf_blockchain()
        
    def retorn_bloques(self):
        return lis_dob

"""
print("****************")
lis_dob = ListaDob()
f_ahora = datetime.datetime.today()
date_now_str = f_ahora.strftime('%d-%m-%y::%H:%M:%S')
#print("*** date_now_str: " + str(date_now_str) )
#insert_inicio(index, timestamp, class_b, data, previous_hash, hash_b):

#lis_dob.insert_inicio(4,1,"inicio1", "jasson4", "5465","as")
#lis_dob.insert_inicio(6,1,"inicio2", "jasson6", "5465","as")

lis_dob.Insert_fin(date_now_str,"estructuras", "jasson1", "5465","as")
lis_dob.Insert_fin(date_now_str,"comp1", "jasson2", "5465","as")
lis_dob.Insert_fin(date_now_str,"ipc1", "jasson3", "5465","as")
 
lis_dob.Insert_fin(date_now_str,"lenguajes", "jasson5", "5465","as")

##lis_dob.delete_inicio()
#lis_dob.Lista_imprimir_atra()
#lis_dob.delete_fin()

lis_dob.Lista_imprimir_ade()
print("*** size: " + str(lis_dob.size) )

lis_dob.graf_blockchain()

#lis_dob.Lista_imprimir_atra()
"""

############

"""
print("1111111  fin para lista lis_dob")
lis_tempo_22 = ListaDob()
lis_tempo_22.Insert_fin(0, 0, "11a")
lis_tempo_22.Insert_fin(0,1,"22a")
lis_tempo_22.Insert_fin(0,2,"33a")
lis_tempo_22.Lista_imprimir_ade()
print("222222  fin para lista lis_tempo_22")
##lis_dob.graf_serpiente()
##lis_dob.Lista_imprimir_atra()
print("imprime otra vez la lista 1")
#lis_dob.Lista_imprimir_ade()

#print("le asigno el valor de lista2 a lista1")
#lis_dob = lis_tempo_22
#lis_dob.Lista_imprimir_ade()
"""