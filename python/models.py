# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrao para perfis de usuarios'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0        

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa %s' % (self.nome,self.telefone,self.empresa)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo,'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis

class Perfil_Vip(Perfil):
    'Classe padrao para perfis de usuarios vips'

    def __init__(self, nome, telefone, empresa, apelido=''):
      super(Perfil_Vip, self).__init__(nome, telefone, empresa)
      self.apelido = apelido

    def obter_creditos(self):
      return super(Perfil_Vip, self).obter_curtidas() * 10.0

class Data(object):

    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime(self):
      print '%s/%s/%s' % (self.dia, self.mes, self.ano)

class Pessoa(object):

    def __init__(self,nome,peso,altura):
        self.nome = nome
        self.peso = float(peso)
        self.altura = float(altura)

    def imprime(self):
        imc = self.peso/(self.altura*2)
        print 'Imc de %s: %s' % (self.nome,imc)

class Conta(object):
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo)

    def calcular_imposto(self): 
        imposto = self.saldo * 0.10
        return imposto

class ContaCorrente(Conta):

    def __init__(self, titular, saldo, bonus):
        super(ContaCorrente, self).__init__(titular, saldo)
        self.bonus = bonus

    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + self.bonus