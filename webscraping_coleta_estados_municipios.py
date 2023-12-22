import requests
from bs4 import BeautifulSoup
from datetime import datetime 
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# def scrap_state_info(state: str) -> dict:
def scrap_state_info(state: str):
    """
    Coleta informações sobre um estado específico do site do IBGE.

    Args:
        state (str): A abreviação do estado (por exemplo, 'sp' para São Paulo).

    Returns:
        dict: Um dicionário contendo as informações coletadas sobre o estado, incluindo seu nome, código, indicadores e data e hora de extração.
    """
        
    print(f'🛸 Coletando informação da UF: {state}')

    state_url = f'https://www.ibge.gov.br/cidades-e-estados/{state}.html'
    page = requests.get(state_url, headers=headers)
        
    soup = BeautifulSoup(page.content, 'html.parser')

    nome = soup.find_all('h1')[1].text
    codigo = soup.find("p","codigo").text.split()[1]

    indicadors = soup.select('.indicador')

    #Criar um dicionário - dict comprehension

    state_dict = {
        ind.select('.ind-label')[0].text: ind.select('.ind-value')[0].text
        for ind in indicadors
    }

    state_dict['Estado'] = nome
    state_dict['Código da UF'] = codigo
    state_dict['Sigla'] = state.upper()
    state_dict['Data de Extração'] = datetime.now().strftime("%Y/%m/%d")
    state_dict['Hora de Extração'] = datetime.now().strftime("%H:%M:%S")


    return state_dict

def scrap_mun_info(uf: str, mun: str):
    """
    Coleta informações de um município específico do Brasil usando web scraping.

    Parâmetros:
    uf (str): A sigla do estado do município.
    mun (str): O nome do município.

    Retorna:
    dict: Um dicionário contendo as informações coletadas do município.

    Exemplo de uso:
    >>> info = scrap_mun_info('MG', 'Belo Horizonte')
    >>> print(info)
    {'População': '2.521.564', 'Área territorial': '331,401 km²', 'Densidade demográfica': '7.610,53 hab/km²', ...}

    """

    print(f'🛸 Coletando informação do município: {mun} - {uf.upper()}')

    mun_url = f'https://www.ibge.gov.br/cidades-e-estados/{uf}/{mun}.html'
    page = requests.get(mun_url, headers=headers)
        
    soup = BeautifulSoup(page.content, 'html.parser')

    nome = soup.find_all('h1')[1].text

    try:
        codigo = soup.find("p","codigo").text.split()[1]
    except:
        codigo = ''

    indicadors = soup.select('.indicador')

    mun_dict = {
        ind.select('.ind-label')[0].text: ind.select('.ind-value')[0].text
        for ind in indicadors
    }

    mun_dict['Município'] = nome
    mun_dict['Município - Verificador'] = mun
    mun_dict['Código do Município'] = codigo
    mun_dict['Data de Extração'] = datetime.now().strftime("%Y/%m/%d")
    mun_dict['Hora de Extração'] = datetime.now().strftime("%H:%M:%S")

    return mun_dict

def data_frame(state_dict):
        """
        Cria um objeto DataFrame a partir de um dicionário de dados.

        Parâmetros:
        state_dict (dict): Um dicionário contendo os dados do estado.

        Retorna:
        DataFrame: Um objeto DataFrame contendo os dados do estado.

        Exemplo:
        >>> data = {'estado': ['SP', 'RJ', 'MG'], 'populacao': [45919049, 17264943, 21168791]}
        >>> df = data_frame(data)
        >>> print(df)
            estado  populacao
        0     SP   45919049
        1     RJ   17264943
        2     MG   21168791
        """

        df = pd.DataFrame(state_dict)

        return df

def get_ano_municipio(df):
    """
    Função que adiciona uma coluna com o ano de cada dado em um DataFrame.

    Parâmetros:
    - df: DataFrame contendo os dados a serem processados.

    Retorno:
    - df_copy: DataFrame com uma nova coluna para cada coluna existente, contendo o ano de cada dado.

    Exemplo de uso:
    df = pd.DataFrame({'Coluna1': ['Dado1', 'Dado2', 'Dado3'],
                       'Coluna2': ['Dado4', 'Dado5', 'Dado6']})
    df_com_ano = get_ano_estado(df)
    """

    df_copy = df.copy()

    cols_nome = df_copy.columns.to_list()

    for col_nome in cols_nome:

        loc = df_copy.columns.get_loc(col_nome) + 1
        nome = col_nome + ' - Ano'
        valor = df_copy[col_nome].str.extract("\[(.*?)\]")

        if col_nome not in ('Gentílico', 'Município', 'Código do Município', 'Data de Extração', 'Hora de Extração'):
            df_copy.insert(loc, nome, valor)
    
    return df_copy

def get_ano_estado(df):
    """
    Função que adiciona uma coluna com o ano de cada dado em um DataFrame.

    Parâmetros:
    - df: DataFrame contendo os dados a serem processados.

    Retorno:
    - df_copy: DataFrame com uma nova coluna para cada coluna existente, contendo o ano de cada dado.

    Exemplo de uso:
    df = pd.DataFrame({'Coluna1': ['Dado1', 'Dado2', 'Dado3'],
                       'Coluna2': ['Dado4', 'Dado5', 'Dado6']})
    df_com_ano = get_ano_estado(df)
    """
    df_copy = df.copy()

    cols_nome = df_copy.columns.to_list()

    for col_nome in cols_nome:

        loc = df_copy.columns.get_loc(col_nome) + 1
        nome = col_nome + ' - Ano'
        valor = df_copy[col_nome].str.extract("\[(.*?)\]")

        if col_nome not in ('Capital', 'Gentílico', 'Estado','Código da UF', 'Sigla', 'Data de Extração', 'Hora de Extração'):
            df_copy.insert(loc, nome, valor)   
    
    return df_copy

def clear_df_estado(df):
    """
    Limpa e formata os dados do DataFrame df.

    Parâmetros:
    - df: DataFrame contendo os dados a serem limpos e formatados.

    Retorna:
    - DataFrame: DataFrame com os dados limpos e formatados.

    Descrição:
    Esta função recebe um DataFrame contendo dados de um estado do Brasil e realiza as seguintes operações:
    - Remove caracteres indesejados dos valores das colunas.
    - Converte os valores das colunas numéricas para o tipo numérico.
    - Retorna o DataFrame com os dados limpos e formatados.

    Observações:
    - Os caracteres removidos incluem pontos, vírgulas, colchetes, unidades de medida e outras informações irrelevantes.
    - As colunas numéricas são especificadas na lista num_col.
    - Na primeira versão do programa, o atributo População estimada e População estimada - Ano eram coletados. 
    - Com a mudança do site, o atributo População residente foi substituído por População estimada, devido o resultado do Censo de 2022.

    """
    
    df = df.replace(
        {
            "\.":"",
            ",":".",
            '\[[^\]]*\]':"",
            ' hab/km²':'',
            "km²":"",
            " pessoas":"",
            ' matrículas':'',
            'R\$.*':'',
            ' veículos':''
        }, 
        regex=True
    )


    num_col = [
                'Área Territorial', 'População residente', 'Densidade demográfica', 
                'Matrículas no ensino fundamental', 'IDH Índice de desenvolvimento humano', 'Receitas realizadas', 
                'Despesas empenhadas', 'Rendimento mensal domiciliar per capita', 'Total de veículos','Código da UF', 'Governador - Ano', 'Área Territorial - Ano',
                'População residente - Ano', 'Densidade demográfica - Ano', 'Matrículas no ensino fundamental - Ano', 
                'IDH Índice de desenvolvimento humano - Ano', 'Receitas realizadas - Ano', 
                'Despesas empenhadas - Ano', 'Rendimento mensal domiciliar per capita - Ano', 'Total de veículos - Ano'
              ]

    df[num_col] = df[num_col].apply(lambda x: x.str.strip())
    df[num_col] = df[num_col].apply(pd.to_numeric)

    return df

def clear_df_municipio(df):

    """
    Limpa e formata os dados do DataFrame df.

    Parâmetros:
    - df: DataFrame contendo os dados a serem limpos e formatados.

    Retorna:
    - DataFrame: DataFrame com os dados limpos e formatados.

    Descrição:
    Esta função recebe um DataFrame contendo dados de um estado do Brasil e realiza as seguintes operações:
    - Remove caracteres indesejados dos valores das colunas.
    - Converte os valores das colunas numéricas para o tipo numérico.
    - Retorna o DataFrame com os dados limpos e formatados.

    Observações:
    - Os caracteres removidos incluem pontos, vírgulas, colchetes, unidades de medida e outras informações irrelevantes.
    - As colunas numéricas são especificadas na lista num_col.
    - Na primeira versão do programa, o atributo População estimada e População estimada - Ano eram coletados. 
    - Com a mudança do site, o atributo População residente foi substituído por População estimada, devido o resultado do Censo de 2022.

    """
    
    df = df.replace(
        {
            "\.":"",
            ",":".",
            '\[[^\]]*\]':"",
            ' hab/km²':'',
            "km²":"",
            " pessoas":"",
            " %":"",
            ' matrículas':'',
            'R\$.*':'',
            ' óbitos por mil nascidos vivos':'',
            "Não informado":''
        }, 
        regex=True
    )


    num_col = [ 
                'Área Territorial', 'População residente', 'Densidade demográfica', 
                'Escolarização 6 a 14 anos', 'IDHM Índice de desenvolvimento humano municipal', 
                'Mortalidade infantil', 'Receitas realizadas', 'Despesas empenhadas', 'PIB per capita','Código do Município',
                'Prefeito - Ano', 'Área Territorial - Ano', 'População residente - Ano', 'Densidade demográfica - Ano', 
                'Escolarização 6 a 14 anos - Ano', 'IDHM Índice de desenvolvimento humano municipal - Ano', 
                'Mortalidade infantil - Ano', 'Receitas realizadas - Ano', 'Despesas empenhadas - Ano', 'PIB per capita - Ano'
              ]

    df[num_col] = df[num_col].apply(lambda x: x.str.strip())
    df[num_col] = df[num_col].apply(lambda x: x.str.replace('-',''))
    #ValueError: Unable to parse string "Não informado" at position 372
    #"Não informado" foi adicionado no dicionário
    df[num_col] = df[num_col].apply(pd.to_numeric)

    return df

def organizar_colunas_estado(df):
    """
    Organiza as colunas do DataFrame de acordo com a ordem especificada e retorna uma cópia do DataFrame organizado.

    Parâmetros:
    - df: DataFrame - O DataFrame contendo os dados a serem organizados.

    Retorno:
    - df_copy: DataFrame - Uma cópia do DataFrame original com as colunas organizadas.

    Exemplo de uso:
    df_organizado = organizar_colunas_estado(df)
    """

    df_copy = df.copy()

    df_copy = df_copy[['Estado', 'Sigla', 'Código da UF', 'Governador', 'Governador - Ano',
                        'Capital', 'Gentílico', 'Área Territorial', 'Área Territorial - Ano',
                        'População residente', 'População residente - Ano', 'Densidade demográfica',
                        'Densidade demográfica - Ano', 'Matrículas no ensino fundamental',
                        'Matrículas no ensino fundamental - Ano', 'IDH Índice de desenvolvimento humano',
                        'IDH Índice de desenvolvimento humano - Ano', 'Receitas realizadas',
                        'Receitas realizadas - Ano', 'Despesas empenhadas',
                        'Despesas empenhadas - Ano', 'Rendimento mensal domiciliar per capita',
                        'Rendimento mensal domiciliar per capita - Ano', 'Total de veículos',
                        'Total de veículos - Ano', 'Data de Extração', 'Hora de Extração']].sort_values(by=['Código da UF'])

    return df_copy
    

def organizar_colunas_municipio(df):
    """
    Organiza as colunas do DataFrame de acordo com a ordem especificada e retorna uma cópia do DataFrame organizado.

    Parâmetros:
    - df: DataFrame - O DataFrame contendo os dados a serem organizados.

    Retorno:
    - df_copy: DataFrame - Uma cópia do DataFrame original com as colunas organizadas.

    Exemplo de uso:
    df_organizado = organizar_colunas_estado(df)
    """
    
    df_copy = df.copy()

    df_copy = df_copy[['Município', 'Município - Verificador', 'Código do Município', 'Prefeito', 'Prefeito - Ano',
                        'Gentílico', 'Área Territorial', 'Área Territorial - Ano', 'População residente',
                        'População residente - Ano', 'Densidade demográfica', 'Densidade demográfica - Ano',
                        'Escolarização 6 a 14 anos', 'Escolarização 6 a 14 anos - Ano', 'IDHM Índice de desenvolvimento humano municipal',
                        'IDHM Índice de desenvolvimento humano municipal - Ano', 'Mortalidade infantil', 'Mortalidade infantil - Ano',
                        'Receitas realizadas', 'Receitas realizadas - Ano', 'Despesas empenhadas', 'Despesas empenhadas - Ano',
                        'PIB per capita', 'PIB per capita - Ano', 'Data de Extração', 'Hora de Extração']].sort_values(by=['Código do Município'])

    return df_copy

def save_to_excel(df_uf, df_mun):
    """
    Salva os dados em um arquivo Excel com duas planilhas, uma para os dados dos estados (UF) e outra para os dados dos municípios (MUN).

    Parâmetros:
    - df_uf (pandas.DataFrame): DataFrame contendo os dados dos estados.
    - df_mun (pandas.DataFrame): DataFrame contendo os dados dos municípios.

    Retorna:
    Nenhum valor de retorno.

    Exemplo de uso:
    save_to_excel(df_uf, df_mun)
    """

    date = datetime.now().strftime("%Y%m%d-%H-%M-%S")
    with pd.ExcelWriter('Informações-cidades-e-estados-IBGE-'+ date + '.xlsx') as writer:
        df_uf.to_excel(writer, sheet_name="UF", index=False )
        df_mun.to_excel(writer, sheet_name="MUN", index=False )

    print('\nParabéns, pesquisa salva!')

if __name__ == '__main__':

    estado = open("estados.txt", 'r', encoding='utf8')
    municipios = open("municipios.txt", 'r', encoding='utf8')
 
    df_estado = data_frame([scrap_state_info(state.strip()) for state in estado])
    df_municipio = data_frame([scrap_mun_info(mun.strip().split()[0], mun.strip().split()[1]) for mun in municipios])
    
    df_estado_ano = get_ano_estado(df_estado)
    df_municipio_ano = get_ano_municipio(df_municipio)

    df_estado_limpo = clear_df_estado(df_estado_ano)
    df_municipio_limpo = clear_df_municipio(df_municipio_ano)

    df_estado_organizado = organizar_colunas_estado(df_estado_limpo)
    df_municipio_organizado = organizar_colunas_municipio(df_municipio_limpo)

    save_to_excel(df_estado_organizado, df_municipio_organizado)

    estado.close()
    municipios.close()




