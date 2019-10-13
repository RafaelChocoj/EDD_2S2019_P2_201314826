import csv

class Import_data:

    def importando(self, dir_archivo):
        encontrado = False
        try:           
            #archivo = open("b2.csv")
            archivo = open(dir_archivo)
            reader = csv.reader(archivo)
            for row in reader:
                print(row)
                """
                #print(row[0] +"="+row[1])
                if row[0] == "CLASS":
                    #print(row[0] +"="+row[1])
                    global class_var
                    class_var = row[1]
                    print("class_var: " + class_var)
                if row[0] == "DATA":
                    #print(row[0] +"="+row[1])
                    global data_var
                    data_var = row[1]
                    print("data_var: " +data_var)
                """

            encontrado = True
        except:
            #print("No existe ruta")
            encontrado = False
        return encontrado
        
    #def retorno_class(self):
    #    return class_var

    #def retorno_data(self):
    #    return data_var

"""
    def new_user(self, name_gamer):
        lis_user.Insert_nod(name_gamer)
"""

impo = Import_data()
impo.importando("b2.csv")
#impo.importando("bloques\\b2.csv")

##lis_user.Lista_imprimir_ade()
##lis_user.graf_users()