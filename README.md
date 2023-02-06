# WebScraping do painel Cidades e Estados do IBGE

![GitHub](https://img.shields.io/github/license/rvidals/WebScraping-cidades-e-estados-IBGE)

Dando continuidade aos meus estudo de Web Scraping, encontrei um vídeo excepcional no [Youtube](https://youtu.be/OpX5Y7dzNjI) de um brasileiro que escreve um algoritmo que faz raspagem por Unidade da Federação no painel [Cidades e Estados](https://www.ibge.gov.br/cidades-e-estados) do IBGE, em que captura uma série de informações interessantes, por exemplo:

  a) Nome do Governador
  b) Capital
  c) Gentílico
  d) Área Territorial
  e) População estimada
  f) Densidade Demográfica
  g) Mátriculas no ensino fundamental
  h) IDH
  i) Receitas realizadas
  j) Despesas empenhadas
  k) Rendimento mensal domiciliar per capita
  l) Total de veículos

O bacana que além de fazer a raspagem é possível fazer um tratamento básico nos dados, como converter dados do tipo objeto para numérico. Gostei bastante, visto que não conhecia a capacidade de usar dicts para realizar várias filtragens de uma única fez usando o .replace do pandas.

# Sobre o projeto

Já que era possível fazer a raspagem para os 26 estados mais o Distrito Federal, totalizando 27 Unidades Federativas (UF), eu pensei: Por que não fazer para os 5.570 municípios também? 
Pois bem, fiz uma série de alterações e criei um algoritmo que além de fazer a raspagem das UF, também faz por município e salva os dois resultados em um único arquivo xlsx, divido por abas - UF e MUN.

As informações adquiridas por município são as seguintes:

  a) Nome do Prefeito
  b) Gentílico
  c) Área Territorial
  d) População estimada
  e) Densidade Demográfica
  f) Escolarização
  g) IDHM
  h) Mortalidade infantil
  i) Receitas realizadas
  j) Despesas empenhadas
  k) PIB per capita

A ideia é rodar o algoritmo de seis em seis meses ou ano a ano e assim gerar um relatório com essas informações. Visto que são informações que não mudam com tanto frequencia, já que necessita de dados atualizados para gerar esses indicadores, por exemplo, o censo demográfico que é gerado de 10 em 10 anos.


# Bibliotecas Utilizadas
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Datetime](https://docs.python.org/3/library/datetime.html)
- [Pandas](https://pandas.pydata.org/)

# Autor
Rogerio Vidal de Siqueira

<a href="https://www.linkedin.com/in/rogerio-vidal-de-siqueira-9478aa136/" target="_blank" rel="noopener noreferrer">Meu Linkdin</a>


