# 🏥 Controle de Insumos Hospitalares com Programação Dinâmica

O **Controle de Insumos Hospitalares** é um projeto em **Python** que aplica **Programação Dinâmica (PD)** para otimizar decisões de **reposição de insumos médicos**, reduzindo custos e evitando desabastecimento.

---

## 🚀 Visão Geral

Hospitais e laboratórios frequentemente enfrentam dois problemas opostos:
- Falta de insumos essenciais;  
- Excesso de materiais que acabam vencendo.

Este projeto modela o problema como um **processo de decisão sequencial**, calculando a **política ótima de pedidos diários** para equilibrar custos de manutenção, reposição e falta de estoque.

---

## 🧩 Como Funciona

A lógica do modelo se baseia em **Programação Dinâmica**, avaliando o custo mínimo esperado ao longo dos dias de planejamento.

### 🔹 Estado
Cada estado representa o dia atual e o nível de estoque:

\[
s = (dia, estoque)
\]

### 🔹 Ação
Decisão de **quanto pedir** no início do dia:

\[
a \ge 0
\]

### 🔹 Transição
Após o consumo diário, o novo estoque é:

\[
estoque' = \max(estoque + a - demanda[dia], 0)
\]

### 🔹 Função Objetivo
Minimizar o custo total esperado:

\[
CustoTotal = \sum_{dia=0}^{N} \big( C_{pedido}(a) + C_{manutencao}(estoque') + C_{falta}(demanda - estoque') \big)
\]

---

## 💻 Implementação

O projeto possui duas versões da PD:

1. **Top-Down (Recursiva com Memoização)** — usa cache para evitar recomputações;  
2. **Bottom-Up (Iterativa)** — preenche a tabela de custos do final para o início.

📄 **Arquivo principal:** `controle_insumos.py`

## 💡 Resultados Esperados

- Política ótima de reposição diária;
- Redução do custo total de operação;
- Melhor previsibilidade do consumo de insumos;
- Possibilidade de adaptar o modelo para múltiplos produtos.

## Tecnologias Utilizadas

- 🐍Python 3.10+
- 📦 functools — memoização da versão recursiva
- 📊 numpy (opcional) — simulações e análise de resultados
- 🧮 Programação Dinâmica — base teórica da otimização

### Exemplo de Função Principal

```python
@functools.lru_cache(maxsize=None)
def dp(dia, estoque):
    if dia == DIAS:
        return 0

    melhor_custo = float('inf')

    for pedido in range(0, MAX_ESTOQUE - estoque + 1):
        estoque_pos_pedido = estoque + pedido
        demanda = DEMANDA_ESPERADA[dia]
        estoque_final = max(estoque_pos_pedido - demanda, 0)

        custo_dia = custo_pedido(pedido) + custo_diario(estoque_final, demanda)
        custo_total = custo_dia + dp(dia + 1, estoque_final)
        melhor_custo = min(melhor_custo, custo_total)

    return melhor_custo
```

## Contribuindo

**Contribuições são muito bem-vindas!**
Se quiser ajudar a melhorar o projeto, siga estes passos:

**1.** Faça um fork do repositório

**2.** Crie uma branch para sua feature
```bash
git checkout -b feature/minha-melhoria
```
**3.** Faça seus commits
```bash
git commit -m "Adiciona nova funcionalidade"
```

**4.** Envie sua branch
```bash
git push origin feature/minha-melhoria
```

Abra um Pull Request 🚀


## Contatos
**Gustavo Coelho**

📧 gustavomcoelho19@gmail.com

🔗 https://github.com/gu7ta2005
