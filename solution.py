# ============================================================
# PROBLEMA: Controle de insumos hospitalares com Programação Dinâmica
# AUTOR: [Seu Nome]
# ============================================================
 
import functools
 
# -------------------------------
# Parâmetros do problema
# -------------------------------
 
DIAS = 7  # horizonte de planejamento (exemplo: 7 dias)
DEMANDA_ESPERADA = [5, 8, 6, 7, 5, 9, 4]  # demanda média por dia
ESTOQUE_INICIAL = 10
 
# Custos
CUSTO_PEDIDO_FIXO = 50      # custo fixo por pedido
CUSTO_MANUTENCAO = 2        # custo por unidade em estoque ao final do dia
CUSTO_FALTA = 10            # custo por unidade não atendida (penalidade)
MAX_ESTOQUE = 20            # limite máximo de armazenamento
 
# -------------------------------
# Funções auxiliares de custo
# -------------------------------
 
def custo_pedido(qtd):
    """Retorna o custo de fazer um pedido de 'qtd' unidades"""
    if qtd > 0:
        return CUSTO_PEDIDO_FIXO
    return 0
 
def custo_diario(estoque_final, demanda_real):
    """
    Calcula o custo diário de manutenção e falta de estoque.
    """
    falta = max(demanda_real - estoque_final, 0)
    manutencao = estoque_final * CUSTO_MANUTENCAO
    return falta * CUSTO_FALTA + manutencao
 
 
# ============================================================
# 🔹 VERSÃO 1: Recursiva com Memoização (Top-Down)
# ============================================================
 
@functools.lru_cache(maxsize=None)
def dp(dia, estoque):
    """
    Retorna o custo mínimo esperado a partir de um dado dia e estoque atual.
    """
    # Caso base: último dia
    if dia == DIAS:
        return 0  # fim do planejamento
 
    melhor_custo = float('inf')
 
    # Testamos todas as quantidades possíveis de pedido (0 até o máximo)
    for pedido in range(0, MAX_ESTOQUE - estoque + 1):
        estoque_pos_pedido = estoque + pedido
        demanda = DEMANDA_ESPERADA[dia]
 
        # Novo estoque após atender a demanda
        estoque_final = max(estoque_pos_pedido - demanda, 0)
 
        # Custo total do dia
        custo_dia = custo_pedido(pedido) + custo_diario(estoque_final, demanda)
 
        # Custo futuro (recursivo)
        custo_total = custo_dia + dp(dia + 1, estoque_final)
 
        melhor_custo = min(melhor_custo, custo_total)
 
    return melhor_custo
 
 
# ============================================================
# 🔹 VERSÃO 2: Iterativa (Bottom-Up)
# ============================================================
 
def dp_iterativa():
    """
    Implementação iterativa (bottom-up) do mesmo problema.
    """
    # dp[t][e] = custo mínimo a partir do dia t com estoque e
    dp = [[float('inf')] * (MAX_ESTOQUE + 1) for _ in range(DIAS + 1)]
 
    # Caso base
    for e in range(MAX_ESTOQUE + 1):
        dp[DIAS][e] = 0  # no último dia, custo futuro é 0
 
    # Preenchemos de trás para frente (do último dia para o primeiro)
    for dia in range(DIAS - 1, -1, -1):
        for estoque in range(MAX_ESTOQUE + 1):
            melhor = float('inf')
            for pedido in range(0, MAX_ESTOQUE - estoque + 1):
                estoque_pos_pedido = estoque + pedido
                demanda = DEMANDA_ESPERADA[dia]
                estoque_final = max(estoque_pos_pedido - demanda, 0)
 
                custo_dia = custo_pedido(pedido) + custo_diario(estoque_final, demanda)
                custo_total = custo_dia + dp[dia + 1][estoque_final]
 
                melhor = min(melhor, custo_total)
            dp[dia][estoque] = melhor
 
    return dp[0][ESTOQUE_INICIAL]
 
 
# ============================================================
# 🔹 Execução e Verificação
# ============================================================
 
if __name__ == "__main__":
    custo_topdown = dp(0, ESTOQUE_INICIAL)
    custo_bottomup = dp_iterativa()
 
    print("Custo mínimo (Recursiva + Memoização):", custo_topdown)
    print("Custo mínimo (Iterativa Bottom-Up):  ", custo_bottomup)
 
    # Checagem de consistência
    assert abs(custo_topdown - custo_bottomup) < 1e-6, "As duas abordagens devem coincidir!"