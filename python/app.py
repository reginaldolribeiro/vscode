# -*- coding: UTF-8 -*-
import re

def cadastrar(nomes):
    print 'Digite: o nome:'
    nome = raw_input()
    nomes.append(nome)

def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):    
        print 'Digite: 1 para cadastrar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar, 0 para terminar '
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)  

        if(escolha == '3'):
            remover(nomes)
        
        if(escolha == '4'):
            alterar(nomes)

        if(escolha == '5'):
            procurar(nomes)

        if(escolha == '6'):
            procurar_regex(nomes)

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def remover(nomes):
    print 'Qual nome voce gostaria de remover?'
    nome = raw_input()
    nomes.remove(nome)

def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome_a_alterar = raw_input()
    indice = nomes.index(nome_a_alterar)
    print 'Digite o novo nome:'
    nome_novo = raw_input()
    nomes[indice] = nome_novo

def procurar(nomes):
    print 'Digite o nome a procurar:'
    nome_a_procurar = raw_input()
    if(nome_a_procurar in nomes):
        print 'Nome %s esta cadastrado' % (nome_a_procurar)
    else:
        print 'Nome %s nao esta cadastrado' % (nome_a_procurar)

''' def alterar(nomes):
    print 'Qual nome vc gostaria de alterar?'
    nome_a_alterar = raw_input()

    if(nome_a_alterar in nomes):
        posicao = nomes.index(nome_a_alterar)
        print 'Digite novo nome:'
        nome_novo = raw_input()
        nomes[posicao] = nome_novo '''

def procurar_regex(nomes):
    print('Digite a expressão regular')
    regex = raw_input()   
    nomes_concatenados = ' '.join(nomes)
    resultados = re.findall(regex,nomes_concatenados)   
    print(resultados)

menu()          