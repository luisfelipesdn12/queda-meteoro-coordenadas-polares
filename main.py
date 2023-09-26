# Luis Felipe Santos do Nascimento - TIA: 32393059
from os import system
from math import pi, cos, sin

definiu_registros = False
unificou_sistemas = False
processou_chuva = False

total_de_quedas_registradas = 0
quedas_dentro_da_propriedade = 0
edificacao_principal_atingida = False
quedas_ne = 0
quedas_no = 0
quedas_so = 0
quedas_se = 0

parar = False
while not parar:

    system("clear")
    i = input(f"""
                                                     
                                *@@@@@@@@@@@#             
                            @@@@@@@@@@@@@@@@@@@@@,        
                        @@@@@@               @@@@@@      
                        @@@@@                     @@@@@    
                        @@@@    @@@@@       @@@@@%   @@@@%  
                    @@@@     @@@@@@     @@@@@@.    @@@@* 
                    @@@@       @@@@@@   @@@@@@       @@@@ 
                    @@@@       @@@ @@@ @@@ @@@       @@@@ 
                    @@@@       @@@  @@@@@, @@@       @@@@ 
                    @@@@     ,@@@,  @@@(  @@@@     @@@@* 
                        @@@@    @@@@@   @%  @@@@@%   @@@@%  
                        @@@@@                     @@@@@    
                        @@@@@@               @@@@@@      
                            @@@@@@@@@@@@@@@@@@@@@/        
                                *@@@@@@@@@@@#             
              
                  Luis Felipe Santos do Nascimento - TIA: 32393059
              
    ================= SISTEMA PARA ANÁLISE DE CHUVA DE METEOROS =================
    ||                                                                         ||
    ||  1. Definir perímetro da propriedade e da edificação de interesse   [{"x" if definiu_registros else " "}] ||
    ||  2. Unificar sistemas de coordenadas de referência                  [{"x" if unificou_sistemas else " "}] ||
    ||  3. Processar registros de chuva de meteoros                        [{"x" if processou_chuva else " "}] ||
    ||  4. Apresentar estatísticas                                             ||
    ||  5. Sair                                                                ||
    ||                                                                         ||
    =============================================================================
    
    Opção => """)

    if i == "1":
        system("clear")
        print("""
        p1 _________
        |           |
        |           | <= propriedade
        |           |
        |_________ p2
        """)
        px1 = int(input("=> Coordenada x do ponto 1 da propriedade: "))
        py1 = int(input("=> Coordenada y do ponto 1 da propriedade: "))
        px2 = int(input("=> Coordenada x do ponto 2 da propriedade: "))
        py2 = int(input("=> Coordenada y do ponto 2 da propriedade: "))

        system("clear")
        print("""
        e1 _________
        |           |
        |           | <= edificação
        |           |
        |_________ e2
        """)
        ex1 = int(input("=> Coordenada x do ponto 1 da edificação: "))
        ey1 = int(input("=> Coordenada y do ponto 1 da edificação: "))
        ex2 = int(input("=> Coordenada x do ponto 2 da edificação: "))
        ey2 = int(input("=> Coordenada y do ponto 2 da edificação: "))
        definiu_registros = True
    elif i == "2":
        if (definiu_registros == True):
            system("clear")
            print("""
            y
            |           
            |    [*]  <= Unidade de Pesquisa
            |           
            |__________ x
            """)
            upx = int(input("=> Coordenada x da Unidade de Pesquisa: "))
            upy = int(input("=> Coordenada y da Unidade de Pesquisa: "))
            unificou_sistemas = True
        else:
            print("\nImpossível processar a unificação no momento: localização da propriedade ainda não informada.")
            input("Aperte <enter> para continuar...")
    elif i == "3":
        if (unificou_sistemas == True):
            processando = True
            while processando:
                system("clear")
                print("""
                             .:'
                         _.::'
              .-;;-.   (_.'
             / ;;;' \\
            |.  `:   | 
             \:   `;/
              '-..-'

    ======= REGISTRO DE QUEDAS DE METEOROS =======
""")

                print(f"Registro #{total_de_quedas_registradas + 1}")
                d = float(input("=> Distância: "))

                if (d < 0):
                    print(f"Fim da coleta de registros: {total_de_quedas_registradas + 1} queda{'s' if total_de_quedas_registradas != 1 else ''} informada{'s' if total_de_quedas_registradas != 1 else ''}.")
                    processando = False
                    continue

                a = float(input("=> Ângulo: "))

                radiano = a * (pi / 180)

                x = round(d * cos(radiano), 2) + upx
                y = round(d * sin(radiano), 2) + upy

                if x >= px1 and x <= px2 and y <= py1 and y >= py2:
                    quedas_dentro_da_propriedade += 1

                    if x >= ex1 and x <= ex2 and y <= ey1 and y >= ey2:
                        edificacao_principal_atingida = True

                if x < 0 and y > 0:
                    quedas_ne += 1
                elif x > 0 and y > 0:
                    quedas_no += 1
                elif x > 0 and y < 0:
                    quedas_so += 1
                elif x < 0 and y < 0:
                    quedas_se += 1
                else:
                    # caiu um uma linha ou no 0, 0
                    pass

                total_de_quedas_registradas += 1

            processou_chuva = True
        else:
            print("\nImpossível processar qualquer registro de queda no momento: localização da propriedade ainda não informada.")
            input("Aperte <enter> para continuar...")
    elif i == "4":
        system("clear")
        print("""
    ⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⠀⠀
    ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡿⡿⠀⠀
    ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⡀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⠀⠀⠀
    ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠋⠙⠷⣦⣄⡀⠀⠀⣴⠟⠀⠀⠀⠀⠀
    ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠈⠙⠳⠾⠋⠀⠀⠀⠀⠀⠀
    ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⡇⠀⠀⣀⡴⠶⣄⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⣇⣴⠞⠉⠀⠀⠈⠳⣤⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⡏⠁⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢸⣇⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⡀⠀
    ⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀
    ======= ESTATÍSTICAS =======
""")
        print(f"""
    Total de quedas registradas: {total_de_quedas_registradas} (100%)
    Quedas dentro da propriedade: {quedas_dentro_da_propriedade} ({(quedas_dentro_da_propriedade * 100)/total_de_quedas_registradas:.2f}%)
    => Quadrante NE: 1 ({(quedas_ne * 100)/total_de_quedas_registradas:.2f}%)
    => Quadrante NO: 7 ({(quedas_no * 100)/total_de_quedas_registradas:.2f}%)
    => Quadrante SO: 5 ({(quedas_so * 100)/total_de_quedas_registradas:.2f}%)
    => Quadrante SE: 2 ({(quedas_se * 100)/total_de_quedas_registradas:.2f}%)
    A edificação principal foi atingida? {"SIM" if edificacao_principal_atingida else "NÃO"}
    """)
        input("Aperte <enter> para continuar...")
    elif i == "5":
        parar = True
    else:
        print("Opção inválida")
