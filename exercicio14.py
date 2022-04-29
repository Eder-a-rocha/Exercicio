peso_diario = 50 #quilos
multa = 4 # reais 

peso_de_peixes = int(input('Peso do peixes: '))
calcule_o_excesso = peso_de_peixes - 50
excedente = calcule_o_excesso * 4

print(f'Quantidade de peixes pescados Kg {peso_de_peixes}')
#print(excedente)

if peso_de_peixes > 50:
    print(f'Quantidade de quilos além do limite {calcule_o_excesso} quilos.')
    print(f'O peso diario foi excedido, multa a ser paga R$ {excedente}')
else:
    print('Peso permitido!')


