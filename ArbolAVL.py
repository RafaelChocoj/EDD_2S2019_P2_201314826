class NodeAVL:
    def __init__(self,value=None):
        self.value=value
        self.h_izq=None
        self.h_der=None
        self.parent=None
        self.height=1
        self.fe = 0

class arbol_AVL:
    def __init__(self):
        self.root = None

    def buscar(self, value):
        if self.root != None:
            return self.buscando_n(value, self.root)
        else:
            return None

    def buscando_n(self, value, node_avl):
        if value == node_avl.value:
            return node_avl
        elif value < node_avl.value and node_avl.h_izq!=None:
            return self.buscando_n(value,node_avl.h_izq )
        elif value > node_avl.value and node_avl.h_der!=None:
            return self.buscando_n(value,node_avl.h_der)
            
    def get_FE(self, node_avl):
        if node_avl == None:
            return -1
        else:
            return node_avl.fe
            
    def get_altura(self, node_avl):
        if node_avl == None:
            return 0
        else:
            return node_avl.height

    #rotacion simpre a la izquierda
    def rot_izquierda(self, z):
        aux = z.h_izq
        z.h_izq = aux.h_der
        aux.h_der = z

        #z.fe = 1 + max(self.get_FE(z.h_izq), self.get_FE(z.h_der))
        #aux.fe = 1 + max(self.get_FE(aux.h_izq), self.get_FE(aux.h_der))

        z.fe = self.get_altura(z.h_der) - self.get_altura(z.h_izq)
        aux.fe = self.get_altura(aux.h_der) - self.get_altura(aux.h_izq)

        z.height = 1 + max(self.get_altura(z.h_izq), self.get_altura(z.h_der))
        aux.height = 1 + max(self.get_altura(aux.h_izq), self.get_altura(aux.h_der))

        return aux

    #rotacion simpre a la derecha
    def rot_derecha(self, z):
        aux = z.h_der
        z.h_der = aux.h_izq
        aux.h_izq = z

        #z.fe = 1 + max(self.get_FE(z.h_izq), self.get_FE(z.h_der))
        #aux.fe = 1 + max(self.get_FE(aux.h_izq), self.get_FE(aux.h_der))

        z.fe = self.get_altura(z.h_der) - self.get_altura(z.h_izq)
        aux.fe = self.get_altura(aux.h_der) - self.get_altura(aux.h_izq)

        z.height = 1 + max(self.get_altura(z.h_izq), self.get_altura(z.h_der))
        aux.height = 1 + max(self.get_altura(aux.h_izq), self.get_altura(aux.h_der))

        return aux

    #rotacion doble ozquierda IZQ-DER
    def rot_doble_izquierda(self, z):
        z.h_izq = self.rot_derecha(z.h_izq)
        temp = self.rot_izquierda(z)
        return temp ############

    #rotacion doble derecja DER-IZQ
    def rot_doble_derecha(self, z):
        z.h_der = self.rot_izquierda(z.h_der)
        temp = self.rot_derecha(z)
        return temp ############

    #insert avl
    def insertAVL(self, new, sub_ar):
        nuevo_parent = sub_ar
        if new.value < sub_ar.value :
            if sub_ar.h_izq == None:
                sub_ar.h_izq = new
            else:
                sub_ar.h_izq = self.insertAVL(new, sub_ar.h_izq)
                #f self.get_FE(sub_ar.h_izq) - self.get_FE(sub_ar.h_der) == 2:
                if self.get_altura(sub_ar.h_izq) - self.get_altura(sub_ar.h_der) == 2:
                    if new.value < sub_ar.h_izq.value:
                        nuevo_parent = self.rot_izquierda(sub_ar)
                    else:
                        nuevo_parent = self.rot_doble_izquierda(sub_ar)

        elif new.value > sub_ar.value:
            if sub_ar.h_der == None:
                sub_ar.h_der = new
            else:
                sub_ar.h_der = self.insertAVL(new, sub_ar.h_der)
                #if self.get_FE(sub_ar.h_der) - self.get_FE(sub_ar.h_izq) == 2:
                if self.get_altura(sub_ar.h_der) - self.get_altura(sub_ar.h_izq) == 2:
                    if new.value > sub_ar.h_der.value:
                        nuevo_parent = self.rot_derecha(sub_ar)
                    else:
                        nuevo_parent = self.rot_doble_derecha(sub_ar)
        else:
            print("node duplicado")

        #update altura
        if sub_ar.h_izq == None and sub_ar.h_der != None:
            sub_ar.fe = self.get_altura(sub_ar.h_der) - 0
            sub_ar.height = sub_ar.h_der.height + 1

        elif sub_ar.h_der == None and sub_ar.h_izq != None:
            sub_ar.fe = 0 - self.get_altura(sub_ar.h_izq)

            sub_ar.height = sub_ar.h_izq.height + 1

        else:
            sub_ar.fe = self.get_altura(sub_ar.h_der) - self.get_altura(sub_ar.h_izq)

            sub_ar.height = 1 + max(self.get_altura(sub_ar.h_izq), self.get_altura(sub_ar.h_der))

        return nuevo_parent


    def insert_nod(self, value):
        new_nod = NodeAVL(value) 

        if self.root == None:
            self.root =  new_nod
        else:
            self.root = self.insertAVL(new_nod, self.root)

    def __repr__(self):
        if self.root==None: return ''
        content='\n' # to hold final string
        cur_nodes=[self.root] # all nodes at current level
        cur_height=self.root.height # height of nodes at current level
        sep=' '*(2**(cur_height-1)) # variable sized separator between elements
        while True:
            cur_height+=-1 # decrement current height
            if len(cur_nodes)==0: break
            cur_row=' '
            next_row=''
            next_nodes=[]
            
            if all(n is None for n in cur_nodes):
                break
            
            for n in cur_nodes:
                if n==None:
                    cur_row+='   '+sep
                    next_row+='   '+sep
                    next_nodes.extend([None,None])
                    continue
                
                if n.value!=None:
                    buf=' '*int((5-len(str(n.value)))/2)
                    cur_row+='%s%s%s'%(buf,str(n.value),buf)+sep
                else:
                    cur_row+=' '*5+sep
                    
                if n.h_izq!=None:
                    next_nodes.append(n.h_izq)
                    next_row+=' /'+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)
                    
                if n.h_der!=None:
                    next_nodes.append(n.h_der)
                    next_row+='\ '+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)
            
            content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
            cur_nodes=next_nodes
            sep=' '*int(len(sep)/2) # cut separator size in half
            
        return content

    def print_tree(self):
        if self.root!=None:
            self._print_tree(self.root)
            
    def _print_tree(self,cur_node):
        if cur_node!=None:
            self._print_tree(cur_node.h_izq)
            print ('%s, h=%d, fe=%d'%(str(cur_node.value),cur_node.height ,cur_node.fe))
            self._print_tree(cur_node.h_der)

ar = arbol_AVL()

ar.insert_nod("mario") 
ar.insert_nod("kart") 
ar.insert_nod("nose")
ar.insert_nod("pa1")
ar.insert_nod("verde")
ar.insert_nod("luig")
ar.insert_nod("lzz")
ar.insert_nod("lz3")
ar.insert_nod("lz5")

"""
ar.insert_nod(40)
ar.insert_nod(50)
ar.insert_nod(25)
"""
print(ar)

ar.print_tree()