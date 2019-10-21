class NodeAVL: 
    def __init__(self, carnet = None, nombre = None): 
        self.carnet = carnet
        self.nombre = nombre
        self.left = None
        self.right = None
        self.height = 1
        self.fe = 0

# AVL arbol
import os
class arbol_AVL: 
  
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert_nod(self, clave, nombre): 
        return self.insert(self.root, clave, nombre)
 
    def insert(self, root_actual, clave, nombre): 
      
        if not root_actual:
            self.root = NodeAVL(clave, nombre) 
            self.size = self.size +1
            return self.root
        elif clave < root_actual.carnet: 
            root_actual.left = self.insert(root_actual.left, clave, nombre) 
        else: 
            root_actual.right = self.insert(root_actual.right, clave, nombre) 
  
        # pas 2 -actulizar altura
        # anterior node 
        root_actual.height = 1 + max(self.get_altura(root_actual.left), 
                           self.get_altura(root_actual.right)) 
  
        # pas 3 - factor fe 
        balance = self.getBalance(root_actual) 
        root_actual.fe =  self.get_altura(root_actual.right) - self.get_altura(root_actual.left) 
  
        # pas 4 - If the node is unbalanced,  

        # 1 - simpre izquierda
        if balance > 1 and clave < root_actual.left.carnet: 
            #return self.rot_derecha(root_actual) 
            self.root = self.rot_derecha(root_actual)
            return self.root
  
        # 2 - simpre derecha
        if balance < -1 and clave > root_actual.right.carnet: 
            #return self.rot_izquierda(root_actual) 
            self.root = self.rot_izquierda(root_actual) 
            return self.root 
  
        # 3 - doble izquierda IZQ-DER
        if balance > 1 and clave > root_actual.left.carnet: 
            root_actual.left = self.rot_izquierda(root_actual.left) 
            #return self.rot_izquierda(root_actual)
            self.root = self.rot_derecha(root_actual)
            return self.root
  
        # 4 - doble derecha DER-IZQ
        if balance < -1 and clave < root_actual.right.carnet: 
            root_actual.right = self.rot_derecha(root_actual.right) 
            #return self.rot_izquierda(root_actual)
            self.root =self.rot_izquierda(root_actual)
            return self.root
  
        self.root = root_actual
        return self.root 
  
    def rot_izquierda(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        #  rotacion 
        y.left = z 
        z.right = T2 
  
        # actulizar altura 
        z.height = 1 + max(self.get_altura(z.left), self.get_altura(z.right)) 
        y.height = 1 + max(self.get_altura(y.left), self.get_altura(y.right)) 

        
        z.fe =  self.get_altura(z.right) - self.get_altura(z.left)  
        y.fe =  self.get_altura(y.right) - self.get_altura(y.left) 
  
        # Return nuevo root
        return y 
  
    def rot_derecha(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # rotation 
        y.right = z 
        z.left = T3 
  
        # actulizar altura 
        z.height = 1 + max(self.get_altura(z.left), self.get_altura(z.right)) 
        y.height = 1 + max(self.get_altura(y.left), self.get_altura(y.right))
                        
        z.fe =  self.get_altura(z.right) - self.get_altura(z.left)  
        y.fe =  self.get_altura(y.right) - self.get_altura(y.left) 
  
        # Return nuevo root 
        return y 
  
    def get_altura(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.get_altura(root.left) - self.get_altura(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.carnet), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 

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
                
                if n.carnet!=None:
                    buf=' '*int((5-len(str(n.carnet)))/2)
                    cur_row+='%s%s%s'%(buf,str(n.carnet),buf)+sep
                else:
                    cur_row+=' '*5+sep
                    
                if n.left!=None:
                    next_nodes.append(n.left)
                    next_row+=' /'+sep
                else:
                    next_row+='  '+sep
                    next_nodes.append(None)
                    
                if n.right!=None:
                    next_nodes.append(n.right)
                    next_row+='\\ '+sep
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
            self._print_tree(cur_node.left)
            print ('%s, h=%d, fe=%d'%(str(cur_node.carnet),cur_node.height ,cur_node.fe ))
            self._print_tree(cur_node.right)

    
    def Graficando_arbol(self):

        f = open("arbol_avl.txt", "w")
        f.write("digraph G { \n")
        f.write("rankdir=TB;\n")
        f.write("graph [nodesep=0.5 ];\n")
        f.write("node [shape = record, fillcolor=seashell2];\n")
        self._VerArbol(f)
        f.write("\n}\n")

        #create_archivo("graf_arbol",grafica_orden);
        f.close()
        os.system("dot -Tpng arbol_avl.txt -o arbol_avl.jpg")
        #os.system("arbol_avl.txt")
        os.system("arbol_avl.jpg")


    def _VerArbol(self, f):
        self.VerArbol(self.root, f)


    def VerArbol(self, root, f): 
        if root != None: 
            self.VerArbol(root.left, f)
            #Node *tempo; 
            tempo = root
            if (tempo.right != None): 
                #tem_nod = tem_nod  +"nodo"+ root.carnet
                #tem_nod = tem_nod  +":C1 -> nodo"+ tempo.right.carnet + "\n"
                          
                f.write("nodo"+ root.carnet)
                f.write(":C1 -> nodo"+ tempo.right.carnet + "\n")
                          
            if (tempo.left != None):
                
                #tem_nod = tem_nod  +"nodo"+ root.carnet
                #tem_nod = tem_nod  +":C0 -> nodo"+ tempo.left.carnet + "\n"
                f.write("nodo"+ root.carnet)
                f.write(":C0 -> nodo"+ tempo.left.carnet + "\n")
                
            #f.write("nodo"+ root.carnet  +" [ label =\"<C0>| carne: "+ root.carnet +"|<C1>\"]; \n")
            f.write("nodo"+ root.carnet  +" [ label =\"<C0>|")
            f.write("Carne: "+ root.carnet + "\\n")
            f.write("Nombre: "+ root.nombre + "\\n")
            ####f.write("Altura: "+ str(root.height)+ "\\n")
            f.write("Altura: "+ str(root.height - 1)+ " ("+str(root.height)+ ")\\n")
            f.write("FE: "+ str(root.fe ))
            f.write("|<C1>\"]; \n")

            self.VerArbol(root.right, f)

    def Graficando_inor(self):
        global index_root
        index_root = 0
        f = open("inorder.txt", "w")
        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape = record, fillcolor=seashell2];\n")
        self._inorder(f)
        f.write("\n}\n")

        #create_archivo("graf_in",grafica_orden)
        f.close()
        os.system("dot -Tpng inorder.txt -o inorder.jpg")
        #os.system("inorder.txt")
        os.system("inorder.jpg")
   
    def _inorder(self, f):
        self.inorder(self.root, f)

    def inorder(self, root, f):
        if (root != None):
            self.inorder(root.left, f)
            global index_root
            index_root = index_root + 1
            if (index_root != self.size):
                #f.write(" \"" + root.carnet + "\" ->")
                f.write(" \"" + root.carnet + "\\n"  + root.nombre + "\" ->")
            else:
                f.write(" \"" + root.carnet + "\\n"  + root.nombre + "\"")
            #cout<< index_root<<"- "<<root->data <<endl;
            self.inorder(root.right, f)
        

    def Graficando_preor(self):
        global index_root
        index_root = 0
        f = open("preorder.txt", "w")
        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape = record, fillcolor=seashell2];\n")

        self._preorder(f)
        f.write("\n}\n")
        #create_archivo("graf_pre",grafica_orden);
        f.close()
        os.system("dot -Tpng preorder.txt -o preorder.jpg")
        #os.system("preorder.txt")
        os.system("preorder.jpg")

    def _preorder(self, f):
        self.preorder(self.root, f)

    def preorder(self, root, f):
        if (root != None):
            global index_root
            index_root = index_root + 1
            if (index_root != self.size):
                f.write(" \"" + root.carnet + "\\n"  + root.nombre + "\" ->")
            else:
                f.write(" \"" + root.carnet + "\\n"  + root.nombre + "\"")

            self.preorder(root.left, f)
            self.preorder(root.right, f)

    ###para pantalla
    def _preorder_con(self):
        global cad
        cad = ""
        global index_root
        index_root = 0
        self.preorder_con(self.root)
        cad = "INICIO -> " + cad  +" -> FIN"
        return cad

    def preorder_con(self, root):
        
        if (root != None):
            global index_root
            index_root = index_root + 1
            global cad
            if (index_root != self.size):
                cad = cad + root.carnet + "-"  + root.nombre + " -> "
            else:
                cad = cad + root.carnet + "-"  + root.nombre + ""

            self.preorder_con(root.left)
            self.preorder_con(root.right)

    def _inorder_con(self):
        global cad
        cad = ""
        global index_root
        index_root = 0
        self.inorder_con(self.root)
        cad = "INICIO -> " + cad  +" -> FIN"
        return cad
        
    def inorder_con(self, root):
        
        if (root != None):

            self.inorder_con(root.left)

            global index_root
            index_root = index_root + 1
            global cad
            if (index_root != self.size):
                cad = cad + root.carnet + "-"  + root.nombre + " -> "
            else:
                cad = cad + root.carnet + "-"  + root.nombre + ""

            self.inorder_con(root.right)
 
    def _postorder_con(self):
        global cad
        cad = ""
        global index_root
        index_root = 0
        self.postorder_con(self.root)
        cad = "INICIO -> " + cad  +" -> FIN"
        return cad
        
    def postorder_con(self, root):
        
        if (root != None):
            
            self.postorder_con(root.left)
            self.postorder_con(root.right)

            global cad
            global index_root
            index_root = index_root + 1
            if (index_root != self.size):
                cad = cad + root.carnet + "-"  + root.nombre + " -> "
            else:
                cad = cad + root.carnet + "-"  + root.nombre + ""

            

    def Graficando_posor(self):
        global index_root
        index_root = 0

        f = open("postorder.txt", "w")
        f.write("digraph G { rankdir=LR\n")
        f.write("node [shape = record, fillcolor=seashell2];\n")

        self._postorder(f)
        f.write("\n}\n")
        #create_archivo("graf_pos",grafica_orden)
        f.close()
        os.system("dot -Tpng postorder.txt -o postorder.jpg")
        #os.system("postorder.txt")
        os.system("postorder.jpg")

    def _postorder(self, f):
        self.postorder(self.root, f)

    def postorder(self, root, f):
        if (root != None):
            self.postorder(root.left, f)
            self.postorder(root.right, f)
            
            global index_root
            index_root = index_root + 1
            if (index_root != self.size):
                f.write(" \"" + root.carnet + "\\n"  + root.nombre + "\" ->")
            else:
                f.write(" \"" + root.carnet + "\\n"  + root.nombre + "\"")

    def insert_ejemplo(self):
        arbol = arbol_AVL()

        arbol.insert_nod("Mario1","12") 
        arbol.insert_nod("Pickachu","13") 
        arbol.insert_nod("Boo","14")
        arbol.insert_nod("Geoff","15")
        arbol.insert_nod("Mario2","16")

        #print("size: " + str(arbol.size))

        #arbol.Graficando_arbol()
        #arbol.Graficando_inor()
        #arbol.Graficando_preor()
        #arbol.Graficando_posor()

"""
arbol = arbol_AVL()
#arbol.insert_nod("mario","mario") 
#arbol.insert_nod("kart","kart") 
#arbol.insert_nod("nose","nose")
#arbol.insert_nod("pa1","pa1")
#arbol.insert_nod("verde","verde")
#arbol.insert_nod("luig","luig")
#arbol.insert_nod("lzz","lzz")
#arbol.insert_nod("lz3","lz3")
#arbol.insert_nod("lz5","lz5")
#arbol.insert_nod("ma","ma")

arbol.insert_nod("Mario1","12") 
arbol.insert_nod("Pickachu","13") 
arbol.insert_nod("Boo","14")
arbol.insert_nod("Geoff","15")
arbol.insert_nod("Mario2","16")

#arbol.insert_nod(40) 
#arbol.insert_nod(50) 
#arbol.insert_nod(25) 

#print(arbol)
print("size: " + str(arbol.size))
#arbol.print_tree()
arbol.Graficando_arbol()
#arbol.Graficando_inor()
#arbol.Graficando_preor()
#arbol.Graficando_posor()
"""