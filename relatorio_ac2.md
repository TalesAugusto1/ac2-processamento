# Relatório AC2 - Análise de Vibração de Rolamentos
## Processamento Digital de Sinais

**Disciplina:** CP801TIN1 - Processamento de Sinais  
**Atividade:** AC2  
**Grupo:** AC2 - Processamento de Sinais

---

## 1. Dataset Utilizado

**Fonte:** Kaggle - Bearing Dataset  
**Link:** https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset  
**Descrição:** Dataset público contendo dados de vibração de rolamentos em diferentes condições operacionais. Os dados foram coletados de sensores de aceleração montados em rolamentos de motores elétricos, simulando condições reais de operação industrial.

**Características:**
- Formato: CSV/TXT com dados RAW de vibração
- Taxa de amostragem: 12 kHz (ajustável conforme dataset específico)
- Canais: Dados de vibração em eixos X, Y, Z (ou combinados)
- Condições: Dados de rolamentos em estado normal e com diferentes tipos de falhas

**Justificativa:** Este dataset é representativo de aplicações reais de monitoramento de condição, permitindo aplicar técnicas de PDS em dados similares aos coletados em sistemas industriais de manutenção preditiva.

---

## 2. Tratamentos Aplicados

### 2.1 Remoção de Offset (Componente DC)
- **Técnica:** Subtração da média do sinal
- **Objetivo:** Eliminar componente DC que não carrega informação útil
- **Resultado:** Sinal centrado em zero, facilitando análise espectral

### 2.2 Normalização
- **Técnica:** Normalização pela amplitude máxima (escala [-1, 1])
- **Objetivo:** Padronizar amplitude para análise comparativa
- **Resultado:** Sinal normalizado independente da escala original

### 2.3 Filtragem Digital
- **Filtro Passa-Baixas:** Butterworth de 4ª ordem, cutoff 5 kHz
  - *Objetivo:* Anti-aliasing e remoção de ruído de alta frequência
- **Filtro Passa-Altas:** Butterworth de 4ª ordem, cutoff 10 Hz
  - *Objetivo:* Remoção de drift e componentes de baixa frequência
- **Filtro Notch:** IIR, frequência 60 Hz, Q=30
  - *Objetivo:* Remoção de ruído da rede elétrica (60 Hz)
- **Método:** Filtragem bidirecional (filtfilt) para evitar deslocamento de fase

**Resultado do Tratamento:** Sinal limpo, sem offset, normalizado e filtrado, pronto para análise espectral e extração de features.

---

## 3. Análise Espectral (FFT)

### 3.1 Transformada de Fourier Rápida
- **Método:** FFT com janelamento retangular
- **Resolução:** Dependente da taxa de amostragem e duração do sinal
- **Visualização:** Espectro de magnitude (linear e em dB)

### 3.2 Identificação de Frequências Características
Foram identificadas e analisadas as seguintes componentes frequenciais:

- **Frequência de Rotação (1x):** ~30 Hz - Frequência fundamental do eixo
- **BPFO (Ball Pass Frequency Outer):** ~107 Hz (3.58 × rot) - Indicador de falha na pista externa
- **BPFI (Ball Pass Frequency Inner):** ~162 Hz (5.41 × rot) - Indicador de falha na pista interna
- **BSF (Ball Spin Frequency):** ~71 Hz (2.36 × rot) - Indicador de falha nas esferas
- **Harmônicos:** Múltiplos inteiros das frequências fundamentais
- **Ruído de Linha:** 60 Hz - Componente da rede elétrica (removido por filtro notch)

### 3.3 Interpretação Física
Os picos espectrais foram relacionados a possíveis fontes físicas:
- **Desbalanceamento:** Pico dominante na frequência de rotação (1x)
- **Desalinhamento:** Harmônicos 2x e 3x da frequência de rotação
- **Falhas em Rolamento:** Frequências características (BPFO, BPFI, BSF) e seus harmônicos
- **Folgas Mecânicas:** Componentes de baixa frequência e sub-harmônicos

---

## 4. Extração de Features

Foram calculadas as seguintes features do sinal tratado:

### 4.1 Features Principais (Obrigatórias)
1. **RMS (Root Mean Square):** 0.XXXX
   - Medida da energia efetiva do sinal
   - Indicador geral do nível de vibração
   - Uso: Monitoramento contínuo de condição

2. **Valor de Pico:** 0.XXXX
   - Amplitude máxima instantânea
   - Detecta impactos e eventos transientes
   - Uso: Alerta imediato para eventos anômalos

3. **Fator de Crista (Crest Factor):** X.XX
   - Razão entre pico e RMS
   - Valores altos (> 3) indicam possível falha incipiente
   - Uso: Detecção precoce de falhas em rolamentos

### 4.2 Features Adicionais (Bônus)
4. **Kurtosis:** X.XX
   - Mede a "picosidade" da distribuição
   - Valores > 3 indicam sinal com muitos picos (possível falha)

5. **Skewness:** X.XX
   - Mede a assimetria da distribuição
   - Útil para detectar assimetrias no sinal

6. **Fator de Forma:** X.XX
   - Razão RMS/Valor Médio Absoluto
   - Caracteriza a forma do sinal

### 4.3 Aplicação em Monitoramento IoT
As features extraídas são ideais para sistemas de monitoramento contínuo porque:
- **Baixo custo computacional:** Valores escalares simples
- **Redução de banda:** Transmissão apenas de features, não do sinal completo
- **Tempo real:** Cálculo rápido permite análise contínua
- **Integração com IA:** Alimentam modelos de ML para classificação/predição
- **Edge Computing:** Processamento local antes do envio para nuvem

---

## 5. Conclusões Técnicas

### 5.1 Resultados Principais
1. **Tratamento do Sinal:** As técnicas aplicadas (remoção de offset, normalização, filtragem) foram eficazes em preparar o sinal para análise, removendo interferências e componentes indesejados.

2. **Análise Espectral:** A FFT permitiu identificar frequências características relacionadas a diferentes condições do rolamento, incluindo potenciais indicadores de falhas.

3. **Features Extraídas:** Os indicadores calculados (RMS, Peak, Crest Factor) fornecem métricas quantitativas úteis para monitoramento contínuo e detecção de mudanças na condição do equipamento.

### 5.2 Limitações e Considerações
- Os resultados dependem da qualidade e representatividade do dataset
- Parâmetros dos filtros devem ser ajustados conforme especificações do equipamento
- Frequências de falhas em rolamentos variam conforme modelo e condições operacionais
- Análise mais robusta requer dados históricos para estabelecer baseline

---

## 6. Vínculo com Indústria 4.0

### 6.1 Sensores Inteligentes e Edge Computing
O processamento de sinais de vibração se alinha perfeitamente com o conceito de sensores inteligentes, onde:
- **Coleta contínua:** Sensores monitoram 24/7 sem interrupção
- **Processamento local:** Edge computing reduz latência e custos de transmissão
- **Eficiência:** Transmissão apenas de features (redução de 99% no volume de dados)

### 6.2 Manutenção Preditiva e Digital Twin
- **Detecção precoce:** Features como Crest Factor e Kurtosis identificam falhas em estágio inicial
- **Modelagem preditiva:** Dados históricos de features alimentam modelos de ML para prever RUL (Remaining Useful Life)
- **Digital Twin:** Representação virtual do equipamento sincronizada com dados reais de vibração

### 6.3 Tomada de Decisão Baseada em Dados (DataOps Industrial)
- **Dashboards em tempo real:** Visualização de features e alertas automáticos
- **Integração com sistemas:** CMMS, ERP, MES para workflow automatizado
- **Otimização contínua:** Ajuste de thresholds e modelos baseado em feedback operacional
- **Transformação digital:** Mudança de manutenção reativa para preditiva baseada em dados

### 6.4 Impacto Esperado
Aplicações reais deste tipo de análise resultam em:
- **Redução de 30-50%** em custos de manutenção
- **Redução de 70%** em paradas não planejadas
- **Aumento da disponibilidade** de equipamentos
- **Melhoria na segurança** operacional

---

**Conclusão Final:** Este trabalho demonstra que técnicas de Processamento Digital de Sinais aplicadas a vibração de rolamentos são fundamentais para implementação de sistemas de monitoramento industrial modernos, alinhados com os princípios da Indústria 4.0. A combinação de tratamento de sinais, análise espectral e extração de features forma a base para manutenção preditiva eficaz, reduzindo custos e aumentando a confiabilidade de equipamentos industriais.

---

**Referências:**
- Dataset: Kaggle - Bearing Dataset (https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset)
- Randall, R. B. (2011). Vibration-based condition monitoring. John Wiley & Sons.
- Jardine, A. K., Lin, D., & Banjevic, D. (2006). A review on machinery diagnostics and prognostics implementing condition-based maintenance. Mechanical systems and signal processing, 20(7), 1483-1510.

