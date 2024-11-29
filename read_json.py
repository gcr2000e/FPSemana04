import json

json_file = input()

try:
 with open(json_file, 'r', encoding='utf-8') as file:
       data = json.load(file)
       print(data)
except:
        print("Ocorreu um erro!")
finally:
        print("Processo concluído")
