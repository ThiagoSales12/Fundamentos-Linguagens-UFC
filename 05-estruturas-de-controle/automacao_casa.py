def automacao_residencial():

    ambiente = {
        "hora": 21, 
        "presenca": True,
        "portas_janelas_abertas": False,
        "temperatura": 27, 
        "movimento_externo": True
    }
    limite_temperatura = 25

    eh_noite = ambiente["hora"] >= 18 or ambiente["hora"] < 6

    print(f"Hora atual: {ambiente['hora']}h")
    print("Presença em casa:", "Sim" if ambiente["presenca"] else "Não")
    print("Portas/janelas abertas:", "Sim" if ambiente["portas_janelas_abertas"] else "Não")
    print(f"Temperatura ambiente: {ambiente['temperatura']}ºC")
    print("Movimento externo detectado:", "Sim" if ambiente["movimento_externo"] else "Não")
    print()
    if not eh_noite:
        print("É dia. Luzes permanecem apagadas.")
    else:
        if ambiente["presenca"]:
            print("É noite e há pessoas. Luzes acesas nos ambientes com presença.")
        else:
            print("É noite e casa vazia. Luzes desligadas.")

    if ambiente["presenca"]:
        if ambiente["temperatura"] > limite_temperatura:
            print("Ar-condicionado ligado.")
        else:
            print("Ar-condicionado desligado (temperatura adequada).")
    else:
        print("Casa vazia. Ar-condicionado desligado para economizar energia.")

    
    if ambiente["portas_janelas_abertas"]:
        print("Alerta! Porta ou janela aberta indevidamente.")
    if eh_noite and ambiente["movimento_externo"]:
        print("Holofotes de segurança ativados na área externa.")
    print()

if __name__ == "__main__":
    automacao_residencial()
