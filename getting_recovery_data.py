import os
import json
import pandas as pd

rootdir = 'C:/Users/wellm/Google Drive (w180947@dac.unicamp.br)/Projetos/Projeto-Become-A-DataScientist/GET-SAMSUNG-DATA/com.samsung.shealth.exercise.recovery_heart_rate'
dataframe_list = list()

# Printa o nome das pastas que contém os arquivos
list_of_files = list(os.listdir(rootdir))

for i in list_of_files:
    # Itera sobre o nome da lista das pastas
    # Adiciona o nome da pasta com todos os arquivos e o nome da pasta única tornando-a uma string
    sub_folders = (f'{str(rootdir)}/{i}')
    # Lista todo os arquivos em cada pasta
    sub_folders_files = os.listdir(sub_folders)

    for i in sub_folders_files:

        # Itera sobre cada arquivo considerando o seu nome e suas pastas
        path_open_file = str(f'{sub_folders}/{i}')

        # Abre o arquivo
        opening = open(str(path_open_file))
        # Lê o Json
        data = json.load(opening)

        try:
            listDictionaries = data['chart_data']
            df = pd.DataFrame(listDictionaries)
            df['id'] = i[0:35]
            dataframe_list.append(df)
        except:
            print(f'Somenthing went wrong on file {i}')

    df_concatenado = pd.concat(dataframe_list, ignore_index=True)
    df_concatenado.to_excel(
        'C:/Users/wellm/Google Drive (w180947@dac.unicamp.br)/Projetos/Projeto-Become-A-DataScientist/GET-SAMSUNG-DATA/output.xlsx')
