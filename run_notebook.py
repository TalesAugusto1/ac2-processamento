#!/usr/bin/env python3
"""
Script para executar todas as células do notebook Jupyter
"""
import json
import sys
import subprocess
from pathlib import Path

def execute_notebook_cells(notebook_path):
    """Executa todas as células de código de um notebook"""
    print(f"Lendo notebook: {notebook_path}")
    
    # Ler o notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Extrair código Python de todas as células
    code_cells = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if source.strip():  # Ignorar células vazias
                code_cells.append(source)
    
    print(f"Encontradas {len(code_cells)} células de código para executar\n")
    print("=" * 60)
    
    # Executar todas as células em sequência
    all_code = '\n\n'.join(code_cells)
    
    # Salvar código temporário
    temp_script = 'temp_notebook_execution.py'
    with open(temp_script, 'w', encoding='utf-8') as f:
        f.write(all_code)
    
    try:
        print("Executando notebook...\n")
        result = subprocess.run(
            [sys.executable, temp_script],
            capture_output=False,
            text=True
        )
        
        if result.returncode == 0:
            print("\n" + "=" * 60)
            print("✓ Notebook executado com sucesso!")
        else:
            print("\n" + "=" * 60)
            print(f"⚠ Notebook executado com código de saída: {result.returncode}")
            
    except Exception as e:
        print(f"\nErro ao executar notebook: {e}")
    finally:
        # Limpar arquivo temporário
        if Path(temp_script).exists():
            Path(temp_script).unlink()

if __name__ == "__main__":
    notebook_path = "ac2_analise_vibracao.ipynb"
    if not Path(notebook_path).exists():
        print(f"Erro: Notebook não encontrado: {notebook_path}")
        sys.exit(1)
    
    execute_notebook_cells(notebook_path)

