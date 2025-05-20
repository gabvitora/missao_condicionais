#1. você está sendo avaliado(a) em sua habilidade de tomar decisões automatizadas por meio de códigos. Em cada uma das atividades a seguir, use estruturas condicionais com sabedoria.
#2 O Sistema de Avaliação da Agência Central de Inteligência precisa classificar os agentes de acordo com sua nota final. Sua missão é automatizar esse processo.
#Solicitar o nome do agente e sua nota final (0 a 10).
#Exibir a classificação:

nome_do_usuario = input('Ola! Seja bem-vindo a nosso Sistema de Avaliação da Agencia Central de Inteligencia, aqui, o nosso trabalho é classificador os agentes. Por favor insira seu nome:')
nota = float (input('Por favor,digite sua nota final:'))


if 9.0 <= nota <= 10.0 :
    print(f'Sr(a){nome_do_usuario}, Excelente 🏅')

elif  7.0 <= nota <= 8.9 :
    print(f'Sr(a) {nome_do_usuario}, Bom 👍')

elif 5.0 <= nota <= 6.9 :
    print(f'Sr(a) {nome_do_usuario}, Regular ⚠️')

elif 3.0 <= nota <= 4.9 :
    print(f'Sr(a) {nome_do_usuario}, Ruim 🚫')

elif 0.0 <= nota <= 2.9 :
    print(f'Sr(a) {nome_do_usuario}, Crítico 🚨')

else:
    print(f'Sr(a){nome_do_usuario}, Nota inválida ❌ ')