# -*- coding: utf-8 -*-
"""62994401364_lista_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rQlipuV7ezxQzEjhcez3U26RGLBCXp8J

![WhatsApp%20Image%202023-09-10%20at%2011.20.28.jpeg](attachment:WhatsApp%20Image%202023-09-10%20at%2011.20.28.jpeg)

# Fala devs, blz??

Esta será nossa quinta lista de exercícios para você testar seu conhecimento acerca do conteúdo do MÓDULO 3:

-Pandas I

## INSTRUÇÕES:

A lista deve ser realizada pelo Jupyter Notebook.

Nâo é necessário entregar a lista para afins de certificado dentro da plataforma, entretanto para alunos da USP que queiram participar do processo seletivo ou conseguir créditos AAC (apenas FEANOS) é necessária a entrega de TODAS as listas.

A entrega das listas ou pelo menos sua excecução é recomendada a fim de exercitar todo o conhecimento adquirido do curso.

O DESAFIO é para realmente te desafiar, por isso não desista de tentar e de continuar com o curso, ao longo das listas você verá que cada vez mais você terá ferramentas para completá-lo.

Caso haja alguma dúvida acerca da lista participe das monitorias que serão oferecidas as quintas e sábados das 17h as 18h pelo DISCORD. Caso seu problema não seje resolvido envie uma mensagem para contato.feadev@gmail.com

O gabarito será disponibilizado na plataforma após o término de periodo de envio
"""

## vamos começar??

"""Toda nossa lista 5 abordará uma temática única de acordo com a base de dados escolhida para a realização da mesma.

**PAÍSES MENOS CORRUPTOS SÃO MAIS FELIZES?**

Será que a felicidade e a corrupção têm alguma relação? A resposta a essa pergunta não é tão clara quanto gostaríamos que fosse. A felicidade é o que todos desejam, enquanto a corrupção é frequentemente vista como algo que a sociedade deve combater. No entanto, a conexão direta entre esses dois conceitos é desafiadora de estabelecer.

A corrupção é prejudicial, pois mina a confiança nas instituições públicas e distorce a alocação de recursos. Isso certamente não soa como um ingrediente para a felicidade. No entanto, em muitos lugares, a corrupção é endêmica, mas as pessoas ainda relatam altos níveis de felicidade. Isso nos faz questionar se a percepção de felicidade pode ser independente da corrupção.

Talvez as pessoas se adaptem à corrupção, ou talvez outros fatores, como economia e segurança, desempenhem um papel mais significativo em sua felicidade. Em última análise, a relação entre felicidade e corrupção é complexa, e as respostas podem variar dependendo do contexto.

Portanto, a questão persiste: **será que a corrupção realmente impede a felicidade? Ou será que a felicidade pode ser encontrada em meio à corrupção?**

vamos utilizar da base de dados Happiness and Corruption 2015-2020

https://www.kaggle.com/datasets/eliasturk/world-happiness-based-on-cpi-20152020

para chegar em alguma conclusão sobre o tema

## QUESTÃO 0

Carregue os dados do arquivo "happiness_corruption.csv" em um DataFrame e mostre as primeiras 5 linhas do DataFrame

baixe a base pelo link abaixo: https://www.kaggle.com/datasets/eliasturk/world-happiness-based-on-cpi-20152020

![Captura%20de%20tela%202023-11-06%20173850.png](attachment:Captura%20de%20tela%202023-11-06%20173850.png)
"""

from google.colab import files

uploaded = files.upload()

import pandas as pd
import io

nome_do_arquivo = 'WorldHappiness_Corruption_2015_2020 (4).csv'
df = pd.read_csv(io.BytesIO(uploaded[nome_do_arquivo]))

df.head()

"""## QUESTÃO 1

**Exploração Inicial dos Dados**

a) Verifique o número de linhas e colunas no DataFrame. **lembre-se do método .shape**
"""

num_linhas, num_colunas = df.shape

print(f'O DataFrame possui {num_linhas} linhas e {num_colunas} colunas.')

"""b) Liste as colunas presentes no DataFrame. **lembre-se do método .columns**

"""

colunas = df.columns

print("Colunas no DataFrame:")
for coluna in colunas:
    print(coluna)

"""c) Verifique se há valores nulos em cada coluna."""

valores_nulos = df.isnull().sum()

print("Valores nulos em cada coluna:")
print(valores_nulos)

"""## QUESTÃO 2

a) Remova as colunas não relevantes que não serão usadas na análise, como "generosity" (generosidade), "family"(familia),
"health"( saúde), "freedom" (liberdade), "dystopia_residual"(distopia residual), "social_support" (suporte social) e "cpi_score"
"""

nome_do_arquivo = 'WorldHappiness_Corruption_2015_2020 (4).csv'
df = pd.read_csv(io.BytesIO(uploaded[nome_do_arquivo]))

# Colunas a serem removidas
colunas_para_remover = ["generosity", "family", "health", "freedom", "dystopia_residual", "social_support", "cpi_score"]

# Remover as colunas especificadas
df_reduzido = df.drop(columns=colunas_para_remover)

# Exibindo as colunas removidas e as primeiras linhas do DataFrame após a remoção
print("Colunas removidas:")
print(colunas_para_remover)

print("DataFrame após a remoção das colunas não relevantes:")
print(df_reduzido.head())

"""b)
Renomeie as colunas para torná-las mais descritivas. Por exemplo, renomeie "Score" para "Pontuacao_Felicidade", "Country" para "Países", "GDP per capita" para "PIB_Per_Capita", "continent" para "Continentes", "Year" para "ano" e government_trust para "confian_gov".
"""

# Renomeando as colunas
df_renomeado = df_reduzido.rename(columns={
    "Country": "Países",
    "happiness_score": "Pontuacao_Felicidade",
    "gdp_per_capita": "PIB_Per_Capita",
    "continent": "Continentes",
    "Year": "Ano",
    "government_trust": "confian_gov"
})

# Exibindo as primeiras linhas do DataFrame com colunas renomeadas
print(df_renomeado.head())

"""## QUESTÃO 3

**Estatísticas Descritivas**

Calcule estatísticas descritivas para as colunas relevantes: "Score" (pontuação de felicidade), "GDP per capita" (PIB per capita) e "Corruption Perception" (percepção de corrupção) e . Mostre a média, mediana, desvio padrão, mínimo e máximo para cada uma dessas colunas.
"""

# Carregue seu arquivo CSV
df = pd.read_csv('WorldHappiness_Corruption_2015_2020 (4).csv')

# Supondo que as colunas de interesse sejam 'happiness_score' (Score), 'gdp_per_capita' (GDP per capita)
# e 'government_trust' (assumindo como percepção de corrupção)
colunas_estatisticas = ['happiness_score', 'gdp_per_capita', 'government_trust']

# Calculando as estatísticas descritivas
estatisticas_descritivas = df[colunas_estatisticas].describe()

# Adicionando a mediana, que não é incluída por padrão no método describe()
mediana = df[colunas_estatisticas].median()
estatisticas_descritivas.loc['median'] = mediana

# Renomeando o índice para incluir a mediana corretamente
estatisticas_descritivas = estatisticas_descritivas.rename(index={'50%': 'median'})

# Exibindo as estatísticas descritivas
print(estatisticas_descritivas)

"""## QUESTÃO 4

Vamos usar somente o ano de 2019 para facilitar a análise.

a) Incluir no dataframe apenas as linhas do ano de 2019
"""

# Filtrando o DataFrame para incluir apenas as linhas do ano de 2019
df_2019 = df[df['Year'] == 2019]

# Exibindo as primeiras linhas do DataFrame filtrado para verificar
print(df_2019.head())

"""b) Criar um novo DataFrame com países que têm pontuação de felicidade acima da média global ( do exercicio anterior)"""

# Calculando a média global da pontuação de felicidade para 2019
media_felicidade_2019 = df_2019['happiness_score'].mean()

# Filtrando o DataFrame para incluir apenas países com pontuação acima da média
df_acima_media = df_2019[df_2019['happiness_score'] > media_felicidade_2019]

# Exibindo as primeiras linhas do novo DataFrame para verificar
print(df_acima_media.head())

"""# QUESTÃO 5

**Classificação**

Classifique o DataFrame resultante do Exercício 4 pela coluna "Score" em ordem decrescente. Mostre os 10 países com as maiores pontuações de felicidade. Isso é útil para responder a perguntas como:

Quais países têm os maiores níveis de felicidade? A classificação em ordem decrescente fornece uma lista dos países com as maiores pontuações de felicidade, destacando aqueles que estão no topo da lista.

Houve alguma mudança significativa na classificação da felicidade ao longo do tempo? Comparando a classificação em diferentes anos, é possível identificar se houve mudanças significativas na pontuação de felicidade de países específicos.

Quais países são modelos de sucesso em termos de felicidade? A classificação ajuda a identificar países que são frequentemente citados como exemplos de sucesso em termos de bem-estar e qualidade de vida.
"""

# Classificando o DataFrame pela coluna "happiness_score" em ordem decrescente
df_classificado = df_acima_media.sort_values(by='happiness_score', ascending=False)

# Exibindo os 10 primeiros países com as maiores pontuações de felicidade
top_10_paises_felizes = df_classificado.head(10)
print(top_10_paises_felizes)

"""## QUESTÃO 6

**Agrupando Dados por Região**

Agrupe os dados por região (coluna "Region") e calcule a média das pontuações de felicidade para cada região. Ordene as regiões pela média de pontuação de felicidade em ordem decrescente.
"""

# Agrupando os dados por região/continente
media_por_regiao = df.groupby('continent')['happiness_score'].mean()

# Ordenando as médias em ordem decrescente
media_por_regiao_ordenada = media_por_regiao.sort_values(ascending=False)

# Exibindo o resultado
print(media_por_regiao_ordenada)

"""## QUESTÃO 7

**Lidando com Dados Ausentes**

Verifique se há dados ausentes no DataFrame e, se houver, retire a linha inteira em questão. Certifique-se de que o DataFrame não possui mais dados ausentes após o preenchimento.
"""

# Carregue seu arquivo CSV
df = pd.read_csv('WorldHappiness_Corruption_2015_2020 (4).csv')

# Verificando dados ausentes
print("Dados ausentes antes da remoção:")
print(df.isna().sum())

# Removendo linhas com dados ausentes
df_limpo = df.dropna()

# Verificando se ainda existem dados ausentes
print("\nDados ausentes após a remoção:")
print(df_limpo.isna().sum())

"""# Questão 8

Agora você tem uma base de dados limpa e com informações relevantes para responder algumas questões.

- Países mais ricos são mais felizes?
- Países com maior confiança no governo (menos experiencias com corrupção) são mais felizes?
- Aonde se localizam os países mais felizes? Europa? Ásia?....

**Países com maior confiança no governo são mais felizes?**

a) Calcule a média da coluna "Confianca_Gov" para obter um valor médio que será usado como ponto de corte.
"""

# Calculando a média da coluna "government_trust"
media_confianca_gov = df['government_trust'].mean()

# Exibindo a média
print("Média de Confiança no Governo (government_trust):", media_confianca_gov)

"""b) Com base na média calculada, crie uma nova coluna no DataFrame que atribuirá um rótulo ("alta" ou "baixa") a cada país de acordo com sua confiança no governo em relação à média."""

# Adicionando uma nova coluna com rótulos "alta" ou "baixa" baseada na confiança no governo
df['confianca_gov_rotulo'] = df['government_trust'].apply(lambda x: 'alta' if x > media_confianca_gov else 'baixa')

# Exibindo as primeiras linhas para verificar a nova coluna
print(df.head())

"""c) Após dividir os países em grupos, calcule a média da pontuação de felicidade para cada grupo separadamente.

"""

# Calculando a média da pontuação de felicidade para países com alta confiança no governo
media_felicidade_alta_confianca = df[df['confianca_gov_rotulo'] == 'alta']['happiness_score'].mean()

# Calculando a média da pontuação de felicidade para países com baixa confiança no governo
media_felicidade_baixa_confianca = df[df['confianca_gov_rotulo'] == 'baixa']['happiness_score'].mean()

# Exibindo as médias
print("Média da Pontuação de Felicidade - Alta Confiança no Governo:", media_felicidade_alta_confianca)
print("Média da Pontuação de Felicidade - Baixa Confiança no Governo:", media_felicidade_baixa_confianca)

"""d) Use um gráfico de barras para representar a relação entre o nível de confiança no governo e a média da pontuação de felicidade. Cada barra no gráfico representa um grupo (alta ou baixa) e a altura da barra representa a média da pontuação de felicidade para esse grupo."""

import matplotlib.pyplot as plt

# Preparando os dados para o gráfico
media_por_grupo = pd.DataFrame({
    'Grupo': ['Alta Confiança no Governo', 'Baixa Confiança no Governo'],
    'Média da Pontuação de Felicidade': [media_felicidade_alta_confianca, media_felicidade_baixa_confianca]
})
media_por_grupo = media_por_grupo.set_index('Grupo')

# Criando o gráfico de barras
plt.figure(figsize=(10, 6))
media_por_grupo.plot(kind='bar', color='skyblue')
plt.title('Média da Pontuação de Felicidade por Nível de Confiança no Governo')
plt.xlabel('Nível de Confiança no Governo')
plt.ylabel('Média da Pontuação de Felicidade')
plt.xticks(rotation=0)
plt.show()

"""e) qual é a conclusão de **Países com maior confiança no governo são mais felizes?**

RESPOSTA:  Países Mais Felizes com Maior Confiança no Governo: Se os dados mostrarem que países com alta confiança no governo têm pontuações de felicidade significativamente maiores, podemos concluir que existe uma tendência de países com maior confiança no governo serem mais felizes. Isso pode ser devido à maior eficiência governamental, menores níveis de corrupção, maior estabilidade e melhores serviços públicos, que contribuem para o bem-estar geral.

Sem Correlação Clara ou Fatores Adicionais: Se as diferenças nas pontuações de felicidade não forem significativas ou se outros fatores parecerem ter um impacto maior, isso sugere que a relação entre confiança no governo e felicidade é mais complexa e pode ser influenciada por múltiplas variáveis.
É importante lembrar que análises como essa podem indicar correlação, mas não necessariamente implicam causalidade. Além disso, a felicidade de um país pode ser influenciada por uma variedade de fatores, incluindo, mas não se limitando a, saúde econômica, sistemas de saúde e educação, liberdade pessoal e cultural, e estabilidade política.

## QUESTÃO 9

**Países mais ricos são mais felizes?**

a) Crie um gráfico de dispersão (scatter plot) que mostre a relação entre a pontuação de felicidade e o PIB per capita. Coloque a pontuação de felicidade no eixo vertical (y) e o PIB per capita no eixo horizontal (x). Adicione rótulos aos eixos e um título informativo ao gráfico.
"""

# Defina os dados para os eixos x e y
x = df['gdp_per_capita']  # Substitua 'gdp_per_capita' pelo nome correto da coluna, se diferente
y = df['happiness_score']  # Substitua 'happiness_score' pelo nome correto da coluna, se diferente

# Crie o gráfico de dispersão
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.scatter(x, y, alpha=0.5)  # Cria o scatter plot com transparência

# Adicione rótulos aos eixos
plt.xlabel('PIB per Capita')
plt.ylabel('Pontuação de Felicidade')
plt.title('Relação entre PIB per Capita e Pontuação de Felicidade')

# Exiba o gráfico
plt.show()

"""b) Qual é a conclusão de **Países mais ricos são mais felizes?**

RESPOSTA: A conclusão sobre se países mais ricos são mais felizes depende dos resultados visualizados no gráfico de dispersão entre o PIB per capita e a pontuação de felicidade. Vamos considerar as possíveis interpretações:

Correlação Positiva: Se o gráfico de dispersão mostrar que, à medida que o PIB per capita aumenta, a pontuação de felicidade também aumenta (ou seja, os pontos no gráfico tendem a subir à medida que se move para a direita), isso sugere uma correlação positiva. Neste caso, podemos concluir que, em média, países mais ricos tendem a ser mais felizes. Isso pode ser devido a fatores como melhor acesso a serviços de saúde, educação, infraestrutura de qualidade e estabilidade econômica, que frequentemente acompanham uma maior riqueza.

Correlação Fraca ou Inexistente: Se o gráfico não mostrar uma tendência clara ou se os pontos estiverem amplamente dispersos sem um padrão definido, isso indicaria uma correlação fraca ou inexistente. Nesse cenário, a conclusão seria que a riqueza (medida pelo PIB per capita) não é necessariamente um determinante confiável da felicidade. Pode haver países com PIB per capita alto, mas com pontuações médias ou baixas de felicidade, e vice-versa.

Outros Fatores em Jogo: É importante lembrar que a felicidade é um fenômeno complexo influenciado por uma variedade de fatores além da riqueza, incluindo cultura, valores sociais, liberdade política e pessoal, qualidade do meio ambiente, entre outros. Portanto, enquanto o PIB per capita é um indicador importante, ele não conta toda a história da felicidade de um país.

Conclusão
A conclusão sobre a relação entre riqueza e felicidade depende da análise do gráfico de dispersão. Se houver uma correlação positiva aparente, pode-se concluir que há uma tendência de países mais ricos serem mais felizes. No entanto, se a correlação for fraca ou inexistente, isso sugere que a riqueza é apenas um dos vários fatores que contribuem para a felicidade. Para uma compreensão mais aprofundada, seria ideal considerar outras variáveis e fatores que também podem influenciar a felicidade dos países.

## QUESTÃO 10

**Aonde se localizam os países mais felizes? Europa? Ásia?....**

a) Calcule a média da pontuação de felicidade (Score) em todo o DataFrame.
"""

# Calculando a média global da pontuação de felicidade
media_felicidade_global = df['happiness_score'].mean()

# Exibindo a média global
print("Média Global da Pontuação de Felicidade:", media_felicidade_global)

"""b) Crie dois DataFrames separados: um com os países com pontuação de felicidade acima da média e outro com os países com pontuação abaixo da média."""

# DataFrames separados para países com pontuação de felicidade acima e abaixo da média
paises_acima_media = df[df['happiness_score'] > media_felicidade_global]
paises_abaixo_media = df[df['happiness_score'] <= media_felicidade_global]

# Exibindo o número de países em cada grupo
print("Número de países com pontuação de felicidade acima da média:", paises_acima_media.shape[0])
print("Número de países com pontuação de felicidade abaixo da média:", paises_abaixo_media.shape[0])

"""c) Para cada um dos dois DataFrames criados no item b, crie subgrupos calculando a contagem de países por continente (coluna "Region"). dica: .value_counts()"""

# Contagem de países por continente para países com pontuação de felicidade acima da média
contagem_continentes_acima_media = paises_acima_media['continent'].value_counts()

# Contagem de países por continente para países com pontuação de felicidade abaixo da média
contagem_continentes_abaixo_media = paises_abaixo_media['continent'].value_counts()

# Exibindo os resultados
print("Contagem de países por continente - Acima da Média de Felicidade:")
print(contagem_continentes_acima_media)
print("\nContagem de países por continente - Abaixo da Média de Felicidade:")
print(contagem_continentes_abaixo_media)

"""d) Calcule a porcentagem que cada continente representa em relação ao total de países em cada grupo."""

# Calculando as porcentagens para países com pontuação de felicidade acima da média
porcentagem_continentes_acima_media = (contagem_continentes_acima_media / len(paises_acima_media)) * 100

# Calculando as porcentagens para países com pontuação de felicidade abaixo da média
porcentagem_continentes_abaixo_media = (contagem_continentes_abaixo_media / len(paises_abaixo_media)) * 100

# Exibindo os resultados
print("Porcentagem de países por continente - Acima da Média de Felicidade:")
print(porcentagem_continentes_acima_media)
print("\nPorcentagem de países por continente - Abaixo da Média de Felicidade:")
print(porcentagem_continentes_abaixo_media)

"""e) Crie gráficos de barras que mostrem a porcentagem de cada continente nos grupos de alta felicidade e baixa felicidade."""

import matplotlib.pyplot as plt

# Gráfico de barras para o grupo de alta felicidade
plt.figure(figsize=(10, 6))
plt.bar(porcentagem_continentes_acima_media.index, porcentagem_continentes_acima_media)
plt.title('Porcentagem de Países por Continente - Acima da Média de Felicidade')
plt.xlabel('Continente')
plt.ylabel('Porcentagem')
plt.xticks(rotation=45)
plt.show()

# Gráfico de barras para o grupo de baixa felicidade
plt.figure(figsize=(10, 6))
plt.bar(porcentagem_continentes_abaixo_media.index, porcentagem_continentes_abaixo_media)
plt.title('Porcentagem de Países por Continente - Abaixo da Média de Felicidade')
plt.xlabel('Continente')
plt.ylabel('Porcentagem')
plt.xticks(rotation=45)
plt.show()

"""f)  Qual é a conclusão da questão: **Aonde se localizam os países mais felizes? Europa? Ásia?....**

RESPOSTA: Para concluir sobre a localização dos países mais felizes com base nos gráficos de barras de porcentagem por continente para grupos de alta e baixa felicidade, você deve observar quais continentes têm a maior porcentagem de países no grupo de alta felicidade. As conclusões podem ser tiradas da seguinte forma:

1. Continente Dominante no Grupo de Alta Felicidade: Se um continente específico, como a Europa, tem uma porcentagem significativamente maior de países no grupo de alta felicidade em comparação com outros continentes, podemos concluir que os países mais felizes tendem a se localizar nesse continente.

2. Diversidade Geográfica da Felicidade: Se os países do grupo de alta felicidade estão mais uniformemente distribuídos entre vários continentes, isso sugere que a felicidade é mais diversificada geograficamente e não está restrita a uma área específica do mundo.

3. Comparação com o Grupo de Baixa Felicidade: Ao observar quais continentes têm maior representação no grupo de baixa felicidade, você pode identificar regiões que podem enfrentar mais desafios em termos de bem-estar e felicidade.

Conclusão:
Se os gráficos mostrarem que um ou dois continentes têm uma proporção muito maior de países no grupo de alta felicidade, isso indica que os países mais felizes tendem a estar concentrados nesses continentes.

Por outro lado, se a distribuição for mais equilibrada, isso indica que a felicidade não está confinada a uma região específica e varia mais amplamente.

Fatores Influenciadores:
É importante lembrar que a felicidade de um país pode ser influenciada por uma variedade de fatores, como estabilidade política, qualidade de vida, liberdade pessoal, saúde econômica e social, entre outros.

Portanto, embora a localização geográfica possa fornecer algumas informações, ela deve ser considerada juntamente com outros fatores que contribuem para o bem-estar de um país.

Com base na análise dos gráficos e informações deste estudo, pode-se concluir que a felicidade é de um conceito complexo ímpar, determinado por uma variedade de fatores diversos, nem sempre podendo ser quantizada ou mesmo qualificada pela estatística. Ela é, portanto, subjetiva, emocional, cultural e pessoal, sendo por fim um sentimento de satisfação com a vida!

APÓS A LISTA VOCÊ CONSEGUE ENXERGAR ALGUMA CONCLUSÃO SOBRE A QUESTÃO INICIAL DO TEMA?

A análise da relação entre corrupção (ou confiança no governo, que frequentemente se relaciona inversamente com a corrupção) e felicidade em países envolve considerar a subjetividade como um fator importante. Aqui estão algumas conclusões que podem ser tiradas com base na lista de sinônimos de subjetividade e na questão inicial:

Percepções Variadas de Corrupção e Felicidade: A subjetividade implica que as percepções de corrupção e felicidade podem variar amplamente entre diferentes culturas e indivíduos. O que é considerado corrupto em uma sociedade pode não ser visto da mesma forma em outra, e o mesmo vale para os conceitos de felicidade.

Influência da Parcialidade e da Perspectiva Pessoal: As opiniões sobre a relação entre corrupção e felicidade podem ser influenciadas por experiências pessoais e culturais. Por exemplo, em sociedades onde a corrupção é mais aceita ou normalizada, pode não haver uma correlação percebida tão forte entre baixa corrupção e alta felicidade.

Relativismo na Avaliação da Felicidade: A felicidade é um conceito altamente relativo e subjetivo. Embora estudos possam mostrar uma tendência de países com menor corrupção serem mais felizes, isso não é uma regra absoluta e pode variar com base em uma série de outros fatores socioculturais e econômicos.

Complexidade da Felicidade e Corrupção: A felicidade é influenciada por múltiplos fatores, e a corrupção é apenas um deles. Outros aspectos como saúde econômica, liberdade individual, qualidade de vida, e saúde e educação podem ter um papel igualmente significativo.

Importância da Individualidade nas Percepções: A individualidade das percepções significa que, mesmo em países menos corruptos, nem todos os cidadãos podem se sentir mais felizes. A experiência de felicidade é pessoal e pode ser influenciada por circunstâncias individuais além da corrupção.

Em resumo, enquanto estudos e análises podem indicar uma tendência geral de países menos corruptos apresentarem níveis mais altos de felicidade, essa relação é complexa e influenciada por fatores subjetivos e culturais. A felicidade e a corrupção são conceitos multifacetados e inter-relacionados, e sua compreensão exige uma abordagem que considere a diversidade de experiências humanas e contextos sociais.
"""

