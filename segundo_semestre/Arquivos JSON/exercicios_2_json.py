import json

with open("segundo_semestre/Arquivos JSON/heroes.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

herois = []

for heroi in dados["members"]:
    if "Flight" in heroi["powers"]:
        herois.append(heroi["name"])

with open("segundo_semestre/Arquivos JSON/herois_voadores.json", "w", encoding="utf-8") as arquivo:
    json.dump(herois, arquivo, indent=4, ensure_ascii=False)

for heroi in herois:
    print(heroi)