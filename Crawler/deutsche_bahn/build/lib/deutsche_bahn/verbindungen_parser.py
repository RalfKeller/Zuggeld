import json

connections = []

with open("Verbindungen.txt",'r',encoding='utf8') as f: 
    verbindungen = f.readlines()
    for verbindung in verbindungen:
        if "-" in verbindung:
            verbindung_array = verbindung.split("-")
            verbindung_dict = {"abfahrt":verbindung_array[0].replace("\n",""),"ankunft":verbindung_array[1].replace("\n","")}
            connections.append(verbindung_dict)

with open("verbindungen.json","w",encoding='utf8') as save:
    json.dump(connections,save,ensure_ascii=False)