

slownik = {'oraz':'i','i':'oraz','prawie nigdy':'nigdy','czemu':'dlaczego'}

# print(slownik['nigdy'])


f= open("text1.txt","r")
text = f.read()


for i in slownik:
    y=slownik[i]

    text = text.replace(y,i)

file = open("test2.txt", "w+")
file.write(text)
