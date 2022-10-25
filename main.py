lista_preferencial = ["Portador de deficiência", "Idosos", "Gestante", "Lactante", "Acompanhado por crianças de colo", "Não abrangente"]
lista_gravidade =[
    ["Reanimação", "Atendimento imediato"],
    ["Emergente", "15 minutos"],
    ["Urgente", "30 minutos"],
    ["Menos urgente", "60 minutos"],
    ["Não urgente", "120 minutos"]
]


cadastros=[["Renan", "12", "3244", "3244", "3244", "3244", "5"]]
fila_preferencial=[]
fila_pediatra=[]
fila_normal=[]



def novo_cadastro():

  nome = input("Insira nome:")
  idade = int(input("Insira idade:"))
  rg = input("Insira RG:")
  endereco = input("Insira endereço:")
  telefone = input("Insira telefone:")
  telefone_emergencia = input("Insira telefone de emergencia:")
  if(idade >= 60):
    indice_preferencial = "Idosos"
  else:
    atendimento_preferencial = input("Atendimento preferencial(s/n):")
    if atendimento_preferencial == "s":
        indice_preferencial = int(input("Categoria de preferencial:"))
    else:
        indice_preferencial = "5"
  cadastros.append([nome, idade, rg, endereco, telefone, telefone_emergencia, indice_preferencial])
  print("Paciente cadastrado com sucesso!\nO número de cadastro é:", len(cadastros))



def agendamento():
    paciente = int(input("Insira o cadastro do paciente:"))
    gravidade_paciente = int(input("Nível de gravidade:"))
    nome_paciente = cadastros[paciente][0]
    idade_paciente = int(cadastros[paciente][1])
    nome_gravidade = lista_gravidade[gravidade_paciente][0]
    tempo_espera = lista_gravidade[gravidade_paciente][1]

    agendamento_preferencial = cadastros[paciente][6]

    if(idade_paciente <= 13):
        fila_pediatra.append([nome_paciente, nome_gravidade, tempo_espera])
        print("Agendamento concluído! O tempo de espera máximo é: "+tempo_espera)
    elif(agendamento_preferencial <= 4):
        fila_preferencial.append([nome_paciente, nome_gravidade, tempo_espera])
        print("Agendamento concluído! O tempo de espera máximo é: "+tempo_espera)
    else:
        fila_normal.append([nome_paciente, nome_gravidade, tempo_espera])
        print("Agendamento concluído! O tempo de espera máximo é: "+tempo_espera)

    print(fila_normal,fila_pediatra,fila_preferencial)


print("SISTEMA DE AGENDAMENTO HOSPITALAR PDA")
fazer_cadastro=input("o paciente tem cadastro?(s/n)")
if(fazer_cadastro == "s"):
  agendamento()
elif(fazer_cadastro=="n"):
  novo_cadastro()


