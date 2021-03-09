def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    # Implemente aqui a lógica da função
    x = 0
    if tempo_chegada1 > tempo_chegada2:
      x = tempo_chegada2
      tempo_chegada_2 = tempo_chegada1
      tempo_chegada1 = x

    if tempo_chegada1 > tempo_chegada3:
      x = tempo_chegada3
      tempo_chegada3 = tempo_chegada1
      tempo_chegada1 = x

    if tempo_chegada2 > tempo_chegada3:
      x = tempo_chegada3
      tempo_chegada3 = tempo_chegada2
      tempo_chegada2 = x
      
    podio = (f"1 - 1 minutos\n"
            f"2 - 2 minutos\n"
            f"3 - 3 minutos\n")

    return podio


