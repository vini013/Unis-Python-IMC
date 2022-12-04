import mysql.connector 
from mysql.connector import Error

print('Bem vindo ao IMC Calculator')
print('Entre com os dados solicitados para calcular o seu IMC')

name = input('Digite seu nome: ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
status = ''

if imc < 17:
  status = 'Muito abaixo do peso'
elif imc >= 17 and imc < 18.5:
  status = 'Abaixo do peso'
elif imc >= 18.5 and imc < 25:
  status = 'Peso normal'
elif imc >= 25 and imc < 30:
  status = 'Acima do peso'
elif imc >= 30 and imc < 35:
  status =  'Obesidade I'
elif imc >= 35 and imc < 40:
  status = 'Obesidade II (severa)'
elif imc >= 40:
  status = 'Obesidade III (mórbida)'


try:
    connection = mysql.connector.connect(host='localhost',database='imc',user='root', password='mysqlpassword' )
    inserir_produtos = """INSERT INTO imc (nome, peso, altura, imc, status) VALUES (""" + "'" + name + "'" + "," + str(peso) + "," + str(altura) + "," + str(imc) + "," + "'" + status + "'" + ")"

    cursor = connection.cursor()
    cursor.execute(inserir_produtos)
    connection.commit()
    print(cursor.rowcount, "Registro inserido com sucesso")
    cursor.close()

except mysql.connector.Error as error:
    print("Falha ao inserir registro no MySQL {}".format(error))

finally:
    if (connection.is_connected()):
      connection.close()
      print("Conexão ao MySQL finalizada")
