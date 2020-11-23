import json

data =''
with open('convertcsv.json') as f:    
    data = json.load(f)


numbers = []


for s in data:
    numbers.append[s['bola1']]
    

"""for s in data:
    numbers.append(s['bola1'])
    numbers.append(s['bola2'])
    numbers.append(s['bola3'])
    numbers.append(s['bola3'])
    numbers.append(s['bola4'])
    numbers.append(s['bola5'])
    numbers.append(s['bola6'])


maiores = []

for n in range(60):
    obj = {"id":n+1,"value":numbers.count(n+1)}
    maiores.append(obj)
  

sorted_list = sorted(maiores, key=lambda k: k['value']) 

for r in sorted_list:
    print r"""




    

