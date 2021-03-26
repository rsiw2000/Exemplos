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
    @staticmethod
    def saudacao(first_up=False):
        iHora = int(datetime.now().strftime("%H"))
        qual = "om dia" if iHora < 12 else "oa tarde" if iHora < 18 else "oa noite"
        return "%s%s" % (("B" if first_up else "b"), qual)
             
    @staticmethod
    def safe_cast(tipo, valor, default=None):
        try:
            return tipo(valor)
        except:
            pass
        return default

def main(args):
    try:
        print ("args", '->', args)
        print ("Testes da classe Util")
        nome = input("Digite seu nome: ")
        print ("%s, %s." % (Util.saudacao(True), nome ))
        idade = input("Qual sua idade: ")
        print ("Ok, entao vc tem %d anos." % (Util.safe_cast(int, idade, 99)))
    except Exception as err:
        print ('Erro no teste - %s' % err)
        sys.exit(1)
    sys.exit(0)


if __name__ == '__main__':
    sys.exit( main( sys.argv ) )
    pass
