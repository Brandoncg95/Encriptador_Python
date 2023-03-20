Frase=input ("Ingrese una frase o palabra: ")

Palabra=Frase

Frase=["a","e","i","o","u"]
listaletras=list(Palabra)
for reemplazo, letras in enumerate(listaletras):
     if letras in Frase and letras != "u":
         listaletras[reemplazo]=Frase[Frase.index(letras)+1]
     if letras in Frase and letras == "u":
         listaletras[reemplazo]=Frase(0)
Frase2 = "".join(listaletras)
print(Frase2)

