# Gráficos Gerados - Análise de Vibração de Rolamentos

Esta pasta contém todos os gráficos gerados durante a execução do notebook `ac2_analise_vibracao.ipynb`.

## Lista de Gráficos

### 01_sinal_bruto.png
- **Descrição:** Visualização do sinal bruto de vibração no domínio do tempo (primeiros 100ms)
- **Tipo:** Gráfico de linha temporal
- **Conteúdo:** Amplitude do sinal de vibração vs tempo

### 02_comparacao_bruto_vs_tratado.png
- **Descrição:** Comparação visual entre o sinal bruto e o sinal tratado
- **Tipo:** Gráfico comparativo (2 subplots)
- **Conteúdo:** 
  - Parte superior: Sinal bruto
  - Parte inferior: Sinal tratado (sem offset, normalizado e filtrado)

### 03_espectro_frequencia.png
- **Descrição:** Espectro de frequência do sinal tratado
- **Tipo:** Gráfico FFT (2 subplots)
- **Conteúdo:**
  - Parte superior: Espectro linear
  - Parte inferior: Espectro em decibéis (dB)

### 04_espectro_com_picos.png
- **Descrição:** Espectro de frequência com picos identificados e anotados
- **Tipo:** Gráfico FFT com anotações
- **Conteúdo:** 
  - Espectro completo
  - Picos identificados marcados em vermelho
  - Anotações com frequências dos principais picos

### 05_features_extraidas.png
- **Descrição:** Visualização das features extraídas do sinal
- **Tipo:** Gráfico de barras horizontais + tabela
- **Conteúdo:**
  - Features principais: RMS, Valor de Pico, Fator de Crista
  - Features adicionais: Kurtosis, Skewness, Fator de Forma
  - Tabela com valores numéricos

### 06_resumo_completo.png
- **Descrição:** Painel resumo completo da análise
- **Tipo:** Grid de subplots (3x2)
- **Conteúdo:**
  - Sinal tratado no tempo
  - Espectro de frequência com picos
  - Features principais (gráfico de barras)
  - Features adicionais (gráfico de barras)

## Especificações Técnicas

- **Formato:** PNG
- **Resolução:** 300 DPI
- **Qualidade:** Alta (bbox_inches='tight')
- **Encoding:** RGB

## Uso

Estes gráficos podem ser utilizados em:
- Relatórios técnicos
- Apresentações
- Documentação do projeto
- Análise visual dos resultados

## Regeneração

Para regenerar os gráficos, execute o notebook novamente:
```bash
python run_notebook.py
```

Ou abra o notebook no Jupyter e execute todas as células:
```bash
jupyter notebook ac2_analise_vibracao.ipynb
```

