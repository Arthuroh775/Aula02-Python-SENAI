#==================================================================================================================
# 1-Quantidade de letras e divisão arredondada

# Criar um programa em Python que peça uma palavra ao usuário, conte quantas letras ela possui e depois
# divida esse número por 3, exibindo o resultado arredondado.

# Solicite ao usuário que digite uma palavra

# Use a função len() para calcular quantas letras essa palavra possui.

# Divida o valor obtido por 3.

# Use a função round() para arredondar o resultado para 2 casas decimais.

# Exiba o tamanho da palavra e o valor da divisão arredondado.



# pa = str(input('Digite uma palavra : '))

# print (f'Essa palavra possui {(len(pa))} letras ')

# calcu = len(pa) / 3

# print(f'Dividindo {len(pa)}/3 quantidade de letras é igual a {calcu}')

# print(f'Arredondando para 2 casas fica {round(calcu,2)}')

#===================================================================================
# 2-Tamanho do nome dividido por 2

# Criar um programa em Python que peça o nome do usuário, conte quantas letras ele tem e mostre esse
# valor dividido por 2, arredondado.

# Peça ao usuário que digite seu nome.

# Use len() para descobrir quantas letras tem o nome.

# Divida esse valor por 2.

# Use round() para arredondar o resultado.

# Mostre na tela o total de letras e o valor arredondado.

name= input('Qual seu nome ?')
print(f'Seu nome têm {len(name)} letras ')
name1 = len(name)/2 
print(f'{len(name)} / 2 = {name1}')
print(f'Arredondando fica igual a {round(name1,2)}')