# Rota Inteligente: Otimização de Entregas com Algoritmos de IA

## 📌 Descrição do Problema

A empresa de delivery Sabor Express enfrenta dificuldades para gerenciar suas entregas durante horários de pico, como almoço e jantar. Atualmente, os trajetos são definidos manualmente pelos entregadores com base apenas em experiência prática, sem o auxílio de ferramentas tecnológicas.

Esse modelo gera rotas ineficientes, atrasos nas entregas, aumento no consumo de combustível e insatisfação dos clientes.

Diante desse cenário, este projeto propõe o desenvolvimento de uma solução baseada em Inteligência Artificial capaz de otimizar as rotas de entrega, reduzindo custos operacionais e melhorando a eficiência logística da empresa.

---

## 🎯 Objetivos do Projeto

O objetivo principal deste projeto é desenvolver um sistema inteligente de otimização de rotas para entregas utilizando algoritmos clássicos de Inteligência Artificial.

Objetivos específicos:

- Modelar a cidade como um grafo
- Encontrar o menor caminho entre pontos de entrega
- Agrupar pedidos próximos para melhorar a eficiência
- Reduzir tempo e distância total das entregas
- Demonstrar a aplicação prática de algoritmos de IA em logística

---

## 🧠 Representação do Problema

A cidade foi representada como um **grafo**, uma estrutura muito utilizada em ciência da computação para representar redes.

Nesse modelo:

- **Nós (Nodes)** representam locais de entrega ou bairros
- **Arestas (Edges)** representam ruas ou caminhos entre locais
- **Pesos (Weights)** representam a distância ou tempo estimado de deslocamento

Essa representação permite que algoritmos de busca encontrem rotas mais eficientes entre diferentes pontos da cidade.

---

## ⚙️ Algoritmos Utilizados

### A* (A-Star)

O algoritmo A* é um algoritmo de busca heurística utilizado para encontrar o menor caminho entre dois pontos em um grafo. Ele combina o custo real do caminho percorrido com uma estimativa heurística da distância restante até o destino.

Esse algoritmo é amplamente utilizado em sistemas de navegação e jogos por sua eficiência.

---

### BFS (Busca em Largura)

A Busca em Largura explora os nós de um grafo nível por nível. Embora não seja o mais eficiente para encontrar o menor caminho em grafos com pesos, é útil para análise estrutural da rede e para fins de comparação.

---

### DFS (Busca em Profundidade)

A Busca em Profundidade percorre um grafo explorando um caminho até o final antes de voltar e testar outras possibilidades. Assim como o BFS, foi utilizado para estudo estrutural do grafo.

---

### K-Means (Clustering)

O algoritmo K-Means foi utilizado para agrupar entregas próximas geograficamente.

Com esse método, os pedidos são organizados em **clusters**, permitindo que cada entregador realize várias entregas próximas em uma única rota, reduzindo deslocamentos desnecessários.

---

## 📊 Metodologia

A solução foi desenvolvida seguindo as seguintes etapas:

1. Modelagem da cidade como um grafo
2. Definição dos pontos de entrega
3. Aplicação do algoritmo A* para encontrar rotas otimizadas
4. Aplicação do algoritmo K-Means para agrupar entregas próximas
5. Comparação entre rotas manuais e rotas otimizadas

---

## 📈 Resultados Esperados

Com a aplicação dos algoritmos de IA, espera-se:

- Redução da distância total percorrida
- Redução do tempo médio de entrega
- Melhor organização das rotas
- Aumento da eficiência operacional

Esses resultados podem gerar impacto direto na satisfação dos clientes e na redução de custos logísticos da empresa.

---

## ⚠️ Limitações do Projeto

Apesar dos benefícios apresentados, o modelo possui algumas limitações:

- Não considera tráfego em tempo real
- Não considera vias interditadas ou mudanças na infraestrutura urbana
- O número de clusters no K-Means precisa ser previamente definido

---

## 🚀 Possíveis Melhorias Futuras

Para tornar o sistema ainda mais robusto, algumas melhorias podem ser implementadas:

- Integração com APIs de mapas (Google Maps ou OpenStreetMap)
- Uso de dados de tráfego em tempo real
- Aplicação de algoritmos genéticos para otimização de rotas
- Implementação de aprendizado por reforço para rotas dinâmicas

---

## 📚 Referências

- UPS ORION – Sistema de otimização de rotas utilizado pela UPS
- Medium – Optimizing Logistics: Clustering e MILP
- ResearchGate – AI-Powered Route Optimization
- Kardinal.ai – Fresh Product Delivery Case Study

---

## 👨‍💻 Tecnologias Utilizadas

- Python
- Algoritmos de grafos
- K-Means Clustering
- Estruturas de dados

---

## 📌 Como Executar o Projeto

1. Clone o repositório

