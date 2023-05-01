# solicita ao usuário as informações necessárias
delta_s = float(input("Informe a variação de espaço em quilômetros: "))
delta_t = float(input("Informe a variação de tempo em horas: "))

# realiza o cálculo da velocidade média
velocidade_media = delta_s / delta_t

# imprime o resultado
print(f"A velocidade média é {velocidade_media:.2f} km/h")
