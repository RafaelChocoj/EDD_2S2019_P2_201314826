import json

from Arbol_AVL import arbol_AVL #para el arbol avl
tree_avl = arbol_AVL()

class Import_json:

    def retorno_tree(self):
        return tree_avl

    def clean_tree(self):
        tree_limpio = arbol_AVL()
        global tree_avl
        tree_avl = tree_limpio

    def read_json(self, dir_archivo):

        ##para leer desde string ya cargado
        data_json = json.loads(dir_archivo)
        #print(data_json)

        self.read_json_preorder(data_json)
        """    
        print(data_json['value'])

        val_ar = data_json['value']
        #val_ar = val_ar.split()
        ##print(val_ar.split("-"))

        #print(val_ar.split("-")[0])
        #print(val_ar.split("-")[1])

        tree_avl.insert_nod(val_ar.split("-")[0],val_ar.split("-")[1]) 
        #print(data_json['left'])
        #print(data_json['rigth'])
        ##print("-------")

        #para recorrer a la izquierda
        if data_json['left'] != None:
            #print("<-*")
            self.read_json_left_a(data_json['left'])

        #para recorrer a la derecha
        if data_json['right'] != None:
            #print("*->")
            self.read_json_rigth_a(data_json['right'])
        """

        #print(data_json['left']['left']['left'])

        #print(type(data_json['value']))
        #print(type(data_json['left']['value']))
        #print(type(data_json['rigth']))

        #tree_avl.Graficando_arbol()

    def read_json_preorder(self, json_izq):
        #data_json = json.loads(json_izq)

        #print(json_izq['value'])

        val_ar = json_izq['value']
        #print(json_izq['value'])
        tree_avl.insert_nod(val_ar.split("-")[0],val_ar.split("-")[1]) 
        #print(json_izq['left'])
        #print(json_izq['rigth'])

        #para recorrer a la izquierda
        if json_izq['left'] != None:
            #print("<-")
            self.read_json_preorder(json_izq['left'])

        #para recorrer a la derecha
        
        if json_izq['right'] != None:
            #print("->")
            self.read_json_preorder(json_izq['right'])

    def read_json_bk_1510(self, dir_archivo):

        ##para leer desde string ya cargado
        data_json = json.loads(dir_archivo)
        #print(data_json)
    
        print(data_json['value'])

        val_ar = data_json['value']
        #val_ar = val_ar.split()
        ##print(val_ar.split("-"))

        #print(val_ar.split("-")[0])
        #print(val_ar.split("-")[1])

        tree_avl.insert_nod(val_ar.split("-")[0],val_ar.split("-")[1]) 
        #print(data_json['left'])
        #print(data_json['rigth'])
        ##print("-------")

        """
        for dat in data_json['left']:
            print("*")
            print(dat['value'])
            #print(dat['left'])
        """
        #para recorrer a la izquierda
        if data_json['left'] != None:
            #print("<-*")
            self.read_json_left_a(data_json['left'])

        #para recorrer a la derecha
        if data_json['right'] != None:
            #print("*->")
            self.read_json_rigth_a(data_json['right'])

        #print(data_json['left']['left']['left'])

        #print(type(data_json['value']))
        #print(type(data_json['left']['value']))
        #print(type(data_json['rigth']))

        #tree_avl.Graficando_arbol()

    def read_json_bk_ruta(self, dir_archivo):

        ###para leer desde ruta arhico
        
        with open(dir_archivo) as data:
            data_json = json.loads(data.read())

            print(data_json)
            print("------")
            print(data_json['INDEX'])
            print(data_json['TIMESTAMP'])
            print(data_json['CLASS'])
            print(data_json['DATA'])
            print(data_json['PREVIOUSHASH'])
            print(data_json['HASH'])




    def read_json_left_a(self, json_izq):
        #data_json = json.loads(json_izq)

        #print(json_izq['value'])

        val_ar = json_izq['value']
        tree_avl.insert_nod(val_ar.split("-")[0],val_ar.split("-")[1]) 
        #print(json_izq['left'])
        #print(json_izq['rigth'])

        #para recorrer a la izquierda
        if json_izq['left'] != None:
            #print("<-")
            self.read_json_left_a(json_izq['left'])

        #para recorrer a la derecha
        
        if json_izq['right'] != None:
            #print("->")
            self.read_json_rigth_a(json_izq['right'])


    def read_json_rigth_a(self, json_der):
        #data_json = json.loads(json_izq)
        #print(json_der['value'])

        val_ar = json_der['value']
        tree_avl.insert_nod(val_ar.split("-")[0],val_ar.split("-")[1])

        #para recorrer a la derecha
        if json_der['right'] != None:
            #print("->")
            self.read_json_rigth_a(json_der['right'])

        #para recorrer a la izquierda
        if json_der['left'] != None:
            #print("<-")
            self.read_json_left_a(json_der['left'])
            

js = Import_json()
js.read_json_bk_ruta('prubb.json')

#tree_avl.Graficando_arbol()
#tree_avl.Graficando_posor()


