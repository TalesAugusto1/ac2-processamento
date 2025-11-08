#!/usr/bin/env python3
"""
Script para inspecionar a estrutura do dataset de vibração de rolamentos
sem precisar carregar todos os dados.
"""

import os
import zipfile
from pathlib import Path
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False
    print("Pandas não disponível. Algumas funcionalidades serão limitadas.")

def inspect_zip_file(zip_path):
    """Inspeciona o conteúdo de um arquivo ZIP sem extrair tudo."""
    print(f"Inspecionando: {zip_path}")
    print("=" * 60)
    
    if not os.path.exists(zip_path):
        print(f"Arquivo não encontrado: {zip_path}")
        return None
    
    file_size = os.path.getsize(zip_path)
    print(f"Tamanho do arquivo: {file_size / (1024*1024):.2f} MB")
    
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            print(f"\nArquivos no dataset ({len(z.filelist)} arquivos):")
            print("-" * 60)
            
            # Listar todos os arquivos
            for i, file_info in enumerate(z.filelist[:30]):  # Primeiros 30
                size_kb = file_info.file_size / 1024
                print(f"  {i+1:2d}. {file_info.filename:<50} {size_kb:>8.2f} KB")
            
            if len(z.filelist) > 30:
                print(f"  ... e mais {len(z.filelist) - 30} arquivos")
            
            # Identificar tipos de arquivos
            print("\n" + "=" * 60)
            print("Análise de tipos de arquivos:")
            print("-" * 60)
            
            extensions = {}
            for file_info in z.filelist:
                ext = Path(file_info.filename).suffix.lower()
                if ext:
                    extensions[ext] = extensions.get(ext, 0) + 1
            
            for ext, count in sorted(extensions.items(), key=lambda x: x[1], reverse=True):
                print(f"  {ext:10s}: {count:4d} arquivos")
            
            # Tentar identificar arquivos de dados principais
            print("\n" + "=" * 60)
            print("Arquivos de dados prováveis:")
            print("-" * 60)
            
            data_files = [f for f in z.filelist if f.filename.endswith(('.csv', '.txt', '.dat', '.mat'))]
            for file_info in data_files[:10]:
                print(f"  - {file_info.filename}")
            
            return z.filelist
            
    except zipfile.BadZipFile:
        print("ERRO: Arquivo não é um ZIP válido!")
        print("O arquivo pode estar corrompido ou incompleto.")
        return None
    except Exception as e:
        print(f"ERRO ao ler arquivo: {e}")
        return None


def inspect_data_file(file_path, sample_lines=5):
    """Inspeciona um arquivo de dados (CSV, TXT, etc.)"""
    print(f"\nInspecionando arquivo de dados: {file_path}")
    print("=" * 60)
    
    if not os.path.exists(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        return None
    
    file_size = os.path.getsize(file_path)
    print(f"Tamanho: {file_size / 1024:.2f} KB")
    
    try:
        if HAS_PANDAS:
            # Tentar ler como CSV
            try:
                df = pd.read_csv(file_path, nrows=100)  # Ler apenas primeiras 100 linhas
                print(f"\nFormato: CSV")
                print(f"Dimensões: {df.shape}")
                print(f"Colunas: {list(df.columns)}")
                print(f"\nPrimeiras {sample_lines} linhas:")
                print(df.head(sample_lines))
                print(f"\nTipos de dados:")
                print(df.dtypes)
                print(f"\nEstatísticas básicas:")
                print(df.describe())
                return df
            except:
                pass
            
            # Tentar ler como TXT (sem cabeçalho)
            try:
                df = pd.read_csv(file_path, header=None, nrows=100, delim_whitespace=True)
                print(f"\nFormato: TXT (sem cabeçalho)")
                print(f"Dimensões: {df.shape}")
                print(f"Colunas: {df.shape[1]} colunas numéricas")
                print(f"\nPrimeiras {sample_lines} linhas:")
                print(df.head(sample_lines))
                print(f"\nTipos de dados:")
                print(df.dtypes)
                return df
            except:
                pass
        
        # Ler como texto puro
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [f.readline() for _ in range(sample_lines)]
            print(f"\nFormato: Texto")
            print(f"Primeiras {sample_lines} linhas:")
            for i, line in enumerate(lines, 1):
                print(f"  {i}: {line.strip()[:100]}")
        
    except Exception as e:
        print(f"ERRO ao ler arquivo: {e}")
        return None


def main():
    """Função principal"""
    print("=" * 60)
    print("INSPETOR DE DATASET - Bearing Dataset")
    print("=" * 60)
    
    # Verificar arquivo ZIP
    zip_path = "data/bearing-dataset.zip"
    
    if os.path.exists(zip_path):
        file_list = inspect_zip_file(zip_path)
        
        # Se conseguirmos listar, tentar extrair e inspecionar um arquivo de exemplo
        if file_list:
            print("\n" + "=" * 60)
            print("Para inspecionar arquivos individuais:")
            print("1. Extraia o dataset: unzip data/bearing-dataset.zip -d data/extracted/")
            print("2. Execute: python inspect_dataset.py <caminho_do_arquivo>")
    
    # Verificar se há arquivos extraídos
    data_dir = Path("data")
    if data_dir.exists():
        extracted_files = list(data_dir.glob("**/*.csv")) + list(data_dir.glob("**/*.txt"))
        if extracted_files:
            print("\n" + "=" * 60)
            print("Arquivos extraídos encontrados:")
            print("-" * 60)
            for f in extracted_files[:5]:
                print(f"  - {f}")
                inspect_data_file(str(f))
    
    print("\n" + "=" * 60)
    print("Inspeção concluída!")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Inspecionar arquivo específico
        inspect_data_file(sys.argv[1])
    else:
        # Inspeção geral
        main()

