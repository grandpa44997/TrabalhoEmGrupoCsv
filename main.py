import csv
import datetime

# Uma lista com as perguntas da pesquisa
PERGUNTAS = [
    "Qual é o seu modal de entrega? (1 - Carro, 2 - Moto ou 3 - Bicicleta)
    "Você se sente seguro(a) ao realizar entregas com seu modal de entrega? (1 - Sim, 2 - Não, 3 - Não sei)",
    "Você recebe treinamento adequado para realizar entregas com seu modal de entrega? (1 - Sim, 2 - Não, 3 - Não sei)",
    "Você consegue atender à demanda de entregas de forma satisfatória com seu modal de entrega? (1 - Sim, 2 - Não, 3 - Não sei)",
    "Você enfrenta dificuldades para encontrar endereços de entrega com seu modal de entrega? (1 - Sim, 2 - Não, 3 - Não sei)",
    "Você acredita que o valor pago pelas entregas é justo considerando seu modal de entrega? (1 - Sim, 2 - Não, 3 - Não sei)",
    "Você recebe apoio adequado da equipe do iFood em caso de problemas durante as entregas com seu modal de entrega? (1 - Sim, 2 - Não, 3 - Não sei)",
    "Você tem acesso a equipamentos de segurança adequados para realizar as entregas com seu modal de entrega? (1 - Sim, 2 - Não, 3 - Não sei)",
    "Você considera o trabalho de entregador do iFood uma opção viável de renda com seu modal de entrega? (1 - Sim, 2 - Não, 3 - Não sei)",
    "Você recomendaria o trabalho de entregador do iFood para outras pessoas com seu modal de entrega? (1 - Sim, 2 - Não, 3 - Não sei)"
]

# Função que recebe as respostas, a idade e o gênero do participante e adiciona a data e hora da resposta
def adicionar_resposta(respostas, idade, genero):
    resposta = [idade, genero] + respostas + [datetime.datetime.now()]  # Cria uma nova lista com a idade, gênero, respostas e data/hora
    return resposta

# Função que escreve as respostas no arquivo CSV
def escrever_csv(respostas):
    with open('respostas.csv', mode='a', newline='') as file:  # Abre o arquivo 'respostas.csv' no modo escrita
        writer = csv.writer(file)  # Cria um objeto writer para escrever no arquivo
        writer.writerow(['Idade', 'Gênero'] + PERGUNTAS + ['Data e hora'])  # Escreve a linha de cabeçalho com as perguntas e data/hora
        for resposta in respostas:  # Para cada resposta:
            writer.writerow(resposta)  # Escreve a resposta no arquivo

# Função que realiza a pesquisa
def fazer_pesquisa():
    respostas = []  # Lista vazia para armazenar as respostas
    while True:
        idade = input("Digite a sua idade (ou 00 para sair): ")  # Pede a idade do participante
        if idade == "00":  # Se o usuário digitar '00', interrompe o laço
            break
        genero = input("Digite o seu gênero (masculino/ feminino/ transgênero/ gênero-neutro/ não-binário/ agênero/ pangênero/ genderqueer/ two-spirit, terceiro gênero): ")  # Pede o gênero do participante
        print("Responda as seguintes perguntas:")
        respostas_participante = []  # Lista vazia para armazenar as respostas do participante
        for pergunta in PERGUNTAS:  # Para cada pergunta da pesquisa:
            resposta = input(pergunta + " ")  # Pede a resposta do participante
            respostas_participante.append(resposta)  # Adiciona a resposta à lista de respostas do participante
        respostas.append(adicionar_resposta(respostas_participante, idade, genero))  # Adiciona a resposta, idade, gênero e data/hora à lista de respostas
    escrever_csv(respostas)  # Escreve as respostas no arquivo CSV
    print("Pesquisa finalizada. Os resultados foram gravados no arquivo respostas.csv.")  # Informa ao usuário que a pesquisa foi finalizada e os resultados foram gravados no arquivo CSV

if __name__ == '__main__':
    fazer_pesquisa()  # Chama a função fazer_pesquisa() se o script for executado diretamente (e não importado como módulo)
