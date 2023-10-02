def mergesort (lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort (lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge (lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
             lista[k] = right[top_right]
             top_right = top_right + 1  

        elif top_left >= len(right):
             lista[k] = right[top_left]
             top_left = top_left + 1  

        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1

        else:
            lista[k] = right[top_right]
            top_right = top_right + 1       

lista = [0, 2, 4, 1, 10]

print (lista)
mergesort (lista)
print (lista)
