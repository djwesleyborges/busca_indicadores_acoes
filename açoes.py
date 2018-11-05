'''
Este script retorna informações de algumas açoes da bovespa.
Pasta você adicionar o codigo da ação na lista, que ele retornara informações da mesma
'''

import requests
from bs4 import BeautifulSoup
l_acoes = ['IBOV11', 'PETR4', 'BBDC4', 'VALE3', 'ITUB4', 'B3SA3', 'BBAS3', 'GGBR4', 'BOVA11', 'ABEV3', 'PETR3', 'LAME4', 'SANB11', 'CMIG4', 'ITSA4', 'BTOW3', 'RAIL3', 'PCAR4', 'AZUL4', 'USIM5']

for a in l_acoes:
    page = requests.get("https://www.guiainvest.com.br/raiox/default.aspx?sigla="+a+"")
    soup = BeautifulSoup(page.text, 'html.parser')
    empresa = soup.find(id='lbNomeEmpresa')
    ultimo_fechamento = soup.find(id='lbUltimoFechamento')
    maxima52s = soup.find(id='lbMaxima52Sem')
    minima52s = soup.find(id='lbMinima52Sem')
    qtd_negocios21d = soup.find(id='lbNumeroNegocioMedio21d')
    volume_medio = soup.find(id='lbVolumeMedio')

    txt_empresa = empresa.text
    txt_ultimo_fechamento = ultimo_fechamento.text
    txt_maxima52s = maxima52s.text
    txt_minima52s = minima52s.text
    txt_qtd_negocios21d = qtd_negocios21d.text
    txt_volume_medio = volume_medio.text

    print(
        "Empresa: " + txt_empresa + "\n",
        "Ultimo Fechamento: " + txt_ultimo_fechamento + "\n",
        "Maxima 52 Semanas: " + txt_maxima52s + "\n",
        "Minima 52 Semanas: " + txt_minima52s + "\n",
        "QtdNegóciado 21dias: " + txt_qtd_negocios21d + "\n",
        "Volume Médio: " + txt_volume_medio + "\n"
    )