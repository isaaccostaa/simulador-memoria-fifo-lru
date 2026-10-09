"""
Simulador de Gerenciamento de Memória
Algoritmos de substituição de páginas: FIFO e LRU
"""


def fifo(paginas, quantidade_frames, mostrar_passos=True):
    """Simula FIFO. Retorna (faltas, hits)."""
    memoria = []  # o início da lista é a página mais antiga
    faltas = 0
    hits = 0

    for pagina in paginas:
        if pagina in memoria:
            hits += 1
            resultado = "HIT"
        else:
            faltas += 1
            resultado = "PAGE FAULT"
            if len(memoria) >= quantidade_frames:
                memoria.pop(0)  # remove a que entrou primeiro
            memoria.append(pagina)

        if mostrar_passos:
            imprimir_passo(pagina, memoria, quantidade_frames, resultado)

    return faltas, hits


def lru(paginas, quantidade_frames, mostrar_passos=True):
    """Simula LRU. Retorna (faltas, hits)."""
    memoria = []  # início = menos recente, fim = mais recente
    faltas = 0
    hits = 0

    for pagina in paginas:
        if pagina in memoria:
            hits += 1
            resultado = "HIT"
            # a página foi usada agora: vira a mais recente
            memoria.remove(pagina)
            memoria.append(pagina)
        else:
            faltas += 1
            resultado = "PAGE FAULT"
            if len(memoria) >= quantidade_frames:
                memoria.pop(0)  # remove a menos recentemente usada
            memoria.append(pagina)

        if mostrar_passos:
            imprimir_passo(pagina, memoria, quantidade_frames, resultado)

    return faltas, hits


def imprimir_passo(pagina, memoria, quantidade_frames, resultado):
    """Mostra uma linha da tabela: Página | Frame 1 | ... | Resultado."""
    frames = [str(p) if i < len(memoria) else "-" for i, p in enumerate(
        memoria + [None] * (quantidade_frames - len(memoria)))]
    colunas = " | ".join(f"{f:^7}" for f in frames)
    print(f"{pagina:^6} | {colunas} | {resultado}")


def imprimir_cabecalho(quantidade_frames):
    colunas = " | ".join(f"{'Frame ' + str(i + 1):^7}" for i in range(quantidade_frames))
    cabecalho = f"{'Página':^6} | {colunas} | Resultado"
    print(cabecalho)
    print("-" * len(cabecalho))


def calcular_taxas(faltas, hits):
    total = faltas + hits
    if total == 0:
        return 0.0, 0.0
    return faltas / total * 100, hits / total * 100


def executar(nome, algoritmo, paginas, quantidade_frames):
    print(f"\n===== {nome} =====")
    imprimir_cabecalho(quantidade_frames)
    faltas, hits = algoritmo(paginas, quantidade_frames, True)
    taxa_fault, taxa_hit = calcular_taxas(faltas, hits)
    print(f"\n{nome}")
    print(f"Page Faults: {faltas}")
    print(f"Hits: {hits}")
    print(f"Taxa de Page Faults: {taxa_fault:.2f}%")
    print(f"Taxa de Hits: {taxa_hit:.2f}%")
    return faltas, hits


def comparar(resultados):
    """resultados: dict nome -> (faltas, hits)."""
    print("\n===== COMPARAÇÃO =====")
    print(f"{'Algoritmo':<10} {'Faults':<8} {'Hits':<8} {'% Faults':<10} {'% Hits':<8}")
    print("-" * 46)
    for nome, (faltas, hits) in resultados.items():
        tf, th = calcular_taxas(faltas, hits)
        print(f"{nome:<10} {faltas:<8} {hits:<8} {tf:<10.2f} {th:<8.2f}")

    f_fifo = resultados["FIFO"][0]
    f_lru = resultados["LRU"][0]
    print()
    if f_fifo < f_lru:
        print(f"Conclusão: o FIFO teve menos page faults ({f_fifo} contra {f_lru}).")
    elif f_lru < f_fifo:
        print(f"Conclusão: o LRU teve menos page faults ({f_lru} contra {f_fifo}).")
    else:
        print(f"Conclusão: empate, os dois tiveram {f_fifo} page faults.")


def ler_entrada():
    while True:
        try:
            entrada = input("Digite as páginas separadas por espaço: ")
            paginas = [int(valor) for valor in entrada.split()]
            if not paginas:
                print("Informe pelo menos uma página.")
                continue
            frames = int(input("Digite a quantidade de frames: "))
            if frames < 1:
                print("A quantidade de frames deve ser pelo menos 1.")
                continue
            return paginas, frames
        except ValueError:
            print("Entrada inválida. Use apenas números inteiros.")


def main():
    paginas, quantidade_frames = ler_entrada()

    print("\nSequência:", paginas)
    print("Frames:", quantidade_frames)

    resultados = {}
    resultados["FIFO"] = executar("FIFO", fifo, paginas, quantidade_frames)
    resultados["LRU"] = executar("LRU", lru, paginas, quantidade_frames)
    comparar(resultados)


if __name__ == "__main__":
    main()
