# Informações sobre o Dataset de Vibração de Rolamentos

## Fonte
**Dataset:** Bearing Dataset  
**Autor:** vinayak123tyagi  
**Plataforma:** Kaggle  
**URL:** https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset

## Estrutura Típica de Datasets de Vibração de Rolamentos

### Formatos Comuns

1. **CSV com cabeçalho**
   ```
   time,vibration_x,vibration_y,vibration_z
   0.000,0.123,0.456,0.789
   0.001,0.124,0.457,0.790
   ```

2. **CSV sem cabeçalho (apenas valores)**
   ```
   0.123
   0.124
   0.125
   ```

3. **TXT com valores separados por espaço**
   ```
   0.000 0.123 0.456 0.789
   0.001 0.124 0.457 0.790
   ```

4. **TXT com valores separados por vírgula**
   ```
   0.000,0.123,0.456,0.789
   0.001,0.124,0.457,0.790
   ```

### Características Esperadas

- **Taxa de amostragem:** Típicamente 12 kHz, 20 kHz, ou 48 kHz
- **Duração:** Variável (segundos a minutos de dados)
- **Canais:** 
  - 1 canal: Vibração total ou RMS
  - 2-3 canais: Vibração em eixos X, Y, Z
  - Múltiplos canais: Diferentes sensores ou condições

### Condições de Dados

Datasets de rolamentos geralmente incluem:
- **Normal:** Dados de rolamentos em condição saudável
- **Falhas:** Dados com diferentes tipos de falhas:
  - Falha na pista externa (Outer Race)
  - Falha na pista interna (Inner Race)
  - Falha nas esferas (Ball)
  - Falha na gaiola (Cage)

## Como Usar o Dataset

### Opção 1: Download Manual
1. Acesse https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset
2. Faça login na sua conta Kaggle
3. Baixe o dataset
4. Extraia os arquivos em `data/`

### Opção 2: Usando Kaggle API
```bash
# Instalar Kaggle CLI
pip install kaggle

# Configurar credenciais (criar ~/.kaggle/kaggle.json)
# Baixar dataset
kaggle datasets download -d vinayak123tyagi/bearing-dataset -p data/

# Extrair
unzip data/bearing-dataset.zip -d data/
```

### Opção 3: Script de Download
```bash
bash download_dataset.sh
```

## Estrutura de Arquivos Esperada

Após extrair, você pode encontrar:

```
data/
├── bearing-dataset.zip
├── normal/
│   ├── normal_001.csv
│   ├── normal_002.csv
│   └── ...
├── inner_race_fault/
│   ├── inner_001.csv
│   └── ...
├── outer_race_fault/
│   └── ...
└── ball_fault/
    └── ...
```

Ou simplesmente:
```
data/
├── bearing_data.csv
├── bearing_data.txt
└── ...
```

## Carregamento no Notebook

O notebook `ac2_analise_vibracao.ipynb` inclui uma função `load_bearing_dataset()` que:

1. **Procura automaticamente** por arquivos CSV, TXT, DAT em `data/`
2. **Tenta diferentes formatos** de carregamento
3. **Normaliza** os dados para o formato esperado (time, vibration)
4. **Fallback** para dados sintéticos se não encontrar arquivos reais

### Uso

O notebook carregará automaticamente os dados se encontrar arquivos em `data/`. Se não encontrar, usará dados sintéticos para demonstração.

## Ajustes Necessários

Após carregar o dataset real, você pode precisar ajustar:

1. **Taxa de amostragem (`SAMPLE_RATE`):**
   ```python
   SAMPLE_RATE = 12000  # Ajuste conforme seu dataset
   ```

2. **Caminho do arquivo:**
   ```python
   DATA_PATH = 'data'  # Ou caminho específico
   ```

3. **Seleção de canal:**
   Se o dataset tiver múltiplos canais (X, Y, Z), escolha qual usar:
   ```python
   # Para usar apenas um canal
   signal_raw = df['vibration_x'].values  # ou 'vibration_y', 'vibration_z'
   
   # Para combinar canais (RMS)
   signal_raw = np.sqrt(df['vibration_x']**2 + df['vibration_y']**2 + df['vibration_z']**2)
   ```

## Notas Importantes

- O dataset requer **autenticação no Kaggle** para download
- O arquivo ZIP pode precisar ser extraído manualmente
- Formatos podem variar - ajuste o código conforme necessário
- Taxa de amostragem deve ser conhecida ou estimada do dataset

## Referências

- [Kaggle Dataset Page](https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset)
- [Kaggle API Documentation](https://www.kaggle.com/docs/api)

