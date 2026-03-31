import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

papel = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

tesoura = '''


    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
lista = ['pedra', 'papel', 'tesoura']

pessoa = int (input ("Vamos jogar pedra, papel e tesoura! Digite 0, para jogar pedra, digite 1 para jogar papel, e digite 2 para jogar tesoura: "))

jogada_computador = random.choice (lista)

if pessoa == 0 and jogada_computador == 'pedra':

    print ("Você jogou:", pedra)

    print ("O computador jogou:", pedra)

    print ("Foi empate!")

elif pessoa == 0 and jogada_computador == 'papel':

    print ("Você jogou:", pedra)

    print ("O computador jogou:", papel)

    print ("Você perdeu!")

elif pessoa == 0 and jogada_computador == 'tesoura':

    print ("Você jogou:", pedra)

    print ("O computador jogou:", tesoura)

    print ("Você ganhou!")

elif pessoa == 1 and jogada_computador == 'papel':

    print ("Você jogou:", papel)

    print ("O computador jogou:", papel)

    print ("Foi empate!")

elif pessoa == 1 and jogada_computador == 'pedra':

    print ("Você jogou:", papel)

    print ("O computador jogou:", pedra)

    print ("Você ganhou!")

elif pessoa == 1 and jogada_computador == 'tesoura':

    print ("Você jogou:", papel)

    print ("O computador jogou:", tesoura)

    print ("Você perdeu!")

elif pessoa == 2 and jogada_computador == 'tesoura':

    print ("Você jogou:", tesoura)

    print ("O computador jogou:", tesoura)

    print ("Foi empate!")

elif pessoa == 2 and jogada_computador == 'pedra':

    print ("Você jogou:", tesoura)

    print ("O computador jogou:", pedra)

    print ("Você perdeu!")

elif pessoa == 2 and jogada_computador == 'papel':

    print ("Você jogou:", tesoura)

    print ("O computador jogou:", papel)

    print ("Você ganhou!")
