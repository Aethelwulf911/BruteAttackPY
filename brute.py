import hashlib
f = open('test', 'r+')
liste = f.readlines()
for i in range(0,len(liste)):
  if hashlib.sha224(liste[i][0:-1].encode('utf-8')).hexdigest() == "abd37534c7d9a2efb9465de931cd7055ffdb8879563ae98078d6d6d5":
    print("ok c'est terminé la reponse : " + liste[i])
    exit() 
print("pas de hash trouvé :( ")
