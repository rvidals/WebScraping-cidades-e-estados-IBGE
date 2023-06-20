# WebScraping do painel Cidades e Estados do IBGE

![GitHub](https://img.shields.io/github/license/rvidals/WebScraping-cidades-e-estados-IBGE)

Dando continuidade aos meus estudo de Web Scraping, encontrei um vídeo excepcional no [Youtube](https://youtu.be/OpX5Y7dzNjI) de um brasileiro que escreve um algoritmo que faz raspagem por Unidade da Federação no painel [Cidades e Estados](https://www.ibge.gov.br/cidades-e-estados) do IBGE, em que captura uma série de informações interessantes, por exemplo:

1.  Nome do Governador
2.  Capital
3.   Gentílico
4.  Área Territorial
5.  População estimada
6.  Densidade Demográfica
7.  Mátriculas no ensino fundamental
8.  IDH
9.  Receitas realizadas
10.  Despesas empenhadas
11.  Rendimento mensal domiciliar per capita
12.  Total de veículos

O bacana que além de fazer a raspagem é possível fazer um tratamento básico nos dados, como converter dados do tipo objeto para numérico. Gostei bastante, visto que não conhecia a capacidade de usar dicts para realizar várias filtragens de uma única fez usando o .replace do pandas.

# Sobre o projeto

Já que era possível fazer a raspagem para os 26 estados mais o Distrito Federal, totalizando 27 Unidades Federativas (UF), eu pensei: Por que não fazer para os 5.570 municípios também? 
Pois bem, fiz uma série de alterações e criei um algoritmo que além de fazer a raspagem das UF, também faz por município e salva os dois resultados em um único arquivo xlsx, divido por abas - UF e MUN.

As informações adquiridas por município são as seguintes:

1.  Nome do Prefeito
2.  Gentílico
3.  Área Territorial
4.  População estimada
5.  Densidade Demográfica
6.  Escolarização
7.  IDHM
8.  Mortalidade infantil
9.  Receitas realizadas
10.  Despesas empenhadas
11.  PIB per capita

A ideia é rodar o algoritmo de seis em seis meses ou ano a ano e assim gerar um relatório com essas informações, visto que  não mudam com tanta frequencia, já que necessita de dados atualizados para gerar esses indicadores, por exemplo, o censo demográfico que é gerado de 10 em 10 anos ou resultado de eleições de 4 a 4 anos.

# Bibliotecas Utilizadas
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Datetime](https://docs.python.org/3/library/datetime.html)
- [Pandas](https://pandas.pydata.org/)

# Autor
Rogerio Vidal de Siqueira

<a href="https://www.linkedin.com/in/rogerio-vidal-de-siqueira-9478aa136/" target="_blank" rel="noopener noreferrer">Meu Linkdin</a>


