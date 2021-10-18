
from os.path import dirname, realpath, isfile 
from json import dump, load

'''
o realpath é usado para pegar o caminho atual do meu arquivo 
o isfile verifica se o arquivo existe ou não 
o dump escreve no json

'''

class JsonManager:

    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/' # AQUI PEGA O ARQUIVO PROPRIAMENTE DITO 
    
    def create_json(self, file):  # METODO PARA CRIAR O JSON PROPRIAMENTE DITO

        data = {"username":"sandro", "password":"1234"}
        path_data_json = self.path + file 

        # Se o arquivo não existir criar 
        if not isfile(path_data_json):
            with open(path_data_json, 'w') as f:
                dump(data, f , indent=2, separators=(',',': '))
            return True
        else:
            return False
    
    # Ler o arquivo Json
    def read_json(self, file):
        if isfile(self.path + file):
            with open(self.path + file) as f: # Abre e lé o arquivo Json 
                data = load(f)
            return data
        else:
            return False 



if __name__ == '__main__':
    jmanager = JsonManager()
    jmanager.create_json('data/data.json')
    data = jmanager.read_json('data/data.json') # ler o conteudo do Json variavel data 
    print(data['username']) # mostra somente o dado que eu coloquei entre ''



