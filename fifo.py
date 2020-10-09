print("Digite a capacidade máxima da lista: ",end="") # Imprimindo uma mensagem 
capacidade = int(input()) # Definindo que a variável capacidade irá receber um valor inteiro
f,falha,top,pf = [],0,0,'Não' # Variáveis
print("Digite todos os elementos que serão inseridos na lista separados por espaço: ",end="") #Imprimindo uma mensagem 
s = list(map(int,input().strip().split())) # Para obter uma lista limpa e organizada que contém números inteiros


print("\nString|Frame →\t",end='')  # Imprimindo uma mensagem 
for i in range(capacidade): # Para cada item dentro de capacidade
    print(i,end=' ') # Desenhar a sequencia da matriz.
print("Falha\n   ↓\n") # E imprimir a mensagem.


#percorre todos os elementos da lista, checa se a lista excedeu a capacidade,
#se não adiciona o elementos, se a lista
#chegou na capacidade maxima ele substitui o elemento mais antigo pelo elemento atual

for i in s: 
    if i not in f: 
        if len(f)<capacidade: 
            f.append(i) 
        else: 
            f[top] = i
            top = (top+1)%capacidade
        falha += 1
        pf = 'Sim'
    else:
        pf = 'Não'
    print("   %d\t\t"%i,end='')
    for x in f:
        print(x,end=' ')
    for x in range(capacidade-len(f)):
        print(' ',end=' ')
    print(" %s"%pf)
print("\nTotal de solicitações: %d\nTotal de solicitações concluídas: %d\nTaxa da sucesso: %0.2f%%"%(len(s),falha,(falha/len(s))*100))