import csv

class Import_data:

    def importando_back(self, dir_archivo):
        encontrado = False
        try:           
            #archivo = open("b2.csv")
            archivo = open(dir_archivo)
            #reader = csv.reader(archivo)
        
            for row in archivo:
            #for row in reader:
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

            archivo.seek(0)
            encontrado = True
        except:
            #print("No existe ruta")
            encontrado = False
        return encontrado
        
    def importando_otro(self, dir_archivo):
        encontrado = False
        try:           
            #archivo = open("b2.csv")
            archivo = open(dir_archivo)
            #reader = csv.reader(archivo)
            #reader = archivo.read()
            #print(reader)
            es_data = False
            global class_var
            global data_var
            class_var = ""
            data_var = ""
            for row in archivo:
            ###for row in reader:
                tempo = row.split(",")
                if tempo[0] == "class":
                    tempo = tempo[1].split("\n")
                    class_var = tempo[0]

                if tempo[0] == "data":
                    
                    #data_var = tempo[1]
                    star = "data,"
                    end = len(row)
                    data_var = row[len(star): end]
                    es_data = True
                elif es_data == True:
                    data_var = data_var + str(row)
                    
            #print("class_var:**" + class_var +"**")
            #print("data_var: **" +data_var+"**")

            archivo.close()
            encontrado = True
        except:
            #print("No existe ruta")
            encontrado = False
        return encontrado

    def importando(self, dir_archivo):
        encontrado = False
        try:           
            #archivo = open("b2.csv")
            archivo = open(dir_archivo)
            reader = csv.reader(archivo)
            for row in reader:
      
                #print(row[0] +"="+row[1])
                if row[0] == "class":
                    #print(row[0] +"="+row[1])
                    global class_var
                    class_var = row[1]
                if row[0] == "data":
                    #print(row[0] +"="+row[1])
                    global data_var
                    data_var = row[1]

            #print("class_var:**" + class_var +"**")
            #print("data_var: **" +data_var+"**")

            encontrado = True
        except:
            #print("No existe ruta")
            encontrado = False
        return encontrado

    def retorno_class(self):
        return class_var

    def retorno_data(self):
        return data_var

"""
    def importando_csv(self, dir_archivo):
        encontrado = False
        try:           
            #archivo = open("b2.csv")
            archivo = open(dir_archivo)
            reader = csv.reader(archivo,delimiter=',')
            #reader = archivo.read()
            #print(reader)
            #es_data = False
            global data_var
            class_var= ""
            data_var = ""
            for row in reader:
                print(row)
                #print(row[0] +"="+row[1])
                if row[0] == "CLASS":
                    #print(row[0] +"="+row[1])
                    class_var = row[1]
                if row[0] == "DATA":
                    #print(row[0] +"="+row[1])
                    data_var = row[1]

            print("class_var:**" + class_var +"**")
            print("data_var: **" +data_var+"**")

            archivo.close()
            encontrado = True

            
        except:
            #print("No existe ruta")
            encontrado = False
        return encontrado
"""

"""
    def new_user(self, name_gamer):
        lis_user.Insert_nod(name_gamer)
"""

"""
impo = Import_data()
impo.importando("b2.csv")
#impo.importando_csv("b2.csv")
#impo.importando("bloques\\b2.csv")

##lis_user.Lista_imprimir_ade()
##lis_user.graf_users()

"""