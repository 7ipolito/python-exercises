## Exercícios de Aprendizado em Python

Repositório de scripts simples usados para praticar fundamentos de Python: tipos de dados, estruturas de repetição, tuplas, listas e pequenos problemas de lógica (incluindo espaço para desafios do LeetCode).

### Estrutura do projeto

```text
python-exercises/
├─ basics/
│  ├─...
└─ leetcode/
```

- **basics**: exercícios introdutórios e práticas rápidas.
- **leetcode**: reservado para soluções de desafios do LeetCode.

### Pré-requisitos

- **Python**: 3.10 ou superior (recomendado 3.11+)
- macOS, Linux ou Windows

### Configuração do ambiente (opcional, mas recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# No Windows (PowerShell): .venv\Scripts\Activate.ps1
python -m pip install -U pip
```

### Como executar os exercícios

Cada arquivo é um script independente. Alguns pedem entrada pelo teclado.

```bash
# Exemplo: rodando um exercício do diretório basics
python basics/par-impar.py

# Outro exemplo
python basics/exercise-fatorial.py
```

- **Dica**: se seu sistema usa `python3` ao invés de `python`, substitua o comando conforme necessário.

### Estilo e organização

- **Nomeação**: arquivos seguem nomes descritivos do que praticam (ex.: `par-impar.py`, `exercise-fatorial.py`).
- **Independência**: scripts não têm dependências externas; focam em lógica e interação via terminal.

### Próximos passos (sugestões)

- Adicionar enunciados e exemplos de I/O no topo de cada arquivo.
- Criar um índice com a lista de exercícios e objetivos de aprendizagem.
- Popular o diretório `leetcode/` com problemas e soluções comentadas.

### Contribuições

Sinta-se à vontade para abrir issues e enviar PRs com melhorias, correções ou novos exercícios.

### Licença

Uso educacional. Defina uma licença (ex.: MIT) caso pretenda compartilhar ou reutilizar amplamente.


