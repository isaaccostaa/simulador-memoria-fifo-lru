# Simulador de Gerenciamento de Memória (FIFO e LRU)

Atividade da Aula 8 — Gerenciamento de Memória.

Simulador em Python de algoritmos de substituição de páginas. O programa recebe uma sequência de páginas e a quantidade de frames, executa **FIFO** e **LRU**, mostra a memória a cada acesso (HIT ou PAGE FAULT) e compara os resultados com taxas de page faults e hits.

## Arquivos

- `simulador_memoria.py`: o simulador, para rodar no terminal.
- `Atividade_Aula_8_Simulador_Memoria.ipynb`: notebook com o código, a execução de exemplo e as respostas das questões de análise.

## Como executar

```bash
python simulador_memoria.py
```

Exemplo de entrada:

```text
Digite as páginas separadas por espaço: 1 2 3 4 1 2 5 1 2 3 4 5
Digite a quantidade de frames: 3
```

Resultado esperado no final (3 frames):

| Algoritmo | Page Faults | Hits |
|-----------|-------------|------|
| FIFO      | 9           | 3    |
| LRU       | 10          | 2    |
