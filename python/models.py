# -*- coding: UTF-8 -*-

class Perfil():
    'Classe padrao para perfis de usuarios'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa %s' % (self.nome,self.telefone,self.empresa)