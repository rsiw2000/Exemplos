# -*- coding: utf-8 -*-
'''
Created on 23 de mar de 2021

@author: Renato Perseguini 
MZ TECNOLOGIA LTDA
'''

import sys
from datetime import datetime

class Util(object):
    # gera uma saudação, bom dia, tarde ou noite
    def saudacao(self, first_up=False):
        iHora = self.safe_cast(int, datetime.now().strftime("%H"), 0)
        qual = "om dia" if iHora < 12 else "oa tarde" if iHora < 18 else "oa noite"
        return "%s%s" % (("B" if first_up else "b"), qual)
             
    # faz um cast com default, sem gerar erro
    def safe_cast(self, tipo, valor, default=None):
        try:
            return tipo(valor)
        except:
            pass
        return default

# rotinas de teste
# Vamos definir a classe de teste dentro da função, para que ela exista somente se a função for chamada
def testes(args):
    # crio uma classe para o processo, que herda as funções da classe Util
    class TesteUtil(Util):
        def executa(self):
            try:
                print ("args", '->', args)
                print ("Testes da classe Util")
                nome = input("Digite seu nome: ")
                print ("%s, %s." % (self.saudacao(True), nome ))
                idade = input("Qual sua idade: ")
                print ("Ok, então vc tem %d anos." % (self.safe_cast(int, idade, 99)))
            except Exception as err:
                print ('Erro no teste - %s' % err)
                
    # então aqui eu vou instanciar e executar o meu processo
    proc = TesteUtil()
    proc.executa()
               

# o nome é __main__ sempre que for executado diretamente (ex.  python Utilidades.py)
# é bom para testes e não interfere quando este módulo for importado a partir de outro
if __name__ == '__main__':
    sys.exit( testes( sys.argv ) )
    pass
