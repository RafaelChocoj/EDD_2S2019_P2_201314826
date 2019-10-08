import json

class Import_json:

    def read_json(self, dir_archivo):

        with open('arjson.json') as data:
            data_json = json.loads(data.read())
            #print("--\n")
            print(data_json)
            
            for dat in data_json:
                print(dat['value'])
            

js = Import_json()
js.read_json("a")