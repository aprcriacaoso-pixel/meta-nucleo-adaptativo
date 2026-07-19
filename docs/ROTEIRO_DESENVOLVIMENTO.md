# 📋 Roteiro Completo de Desenvolvimento do MNA

## Fase 1: Fundação (✅ CONCLUÍDO)

### Sprint 1.1: Arquitetura Base
- ✅ Meta-Núcleo Adaptativo (core)
- ✅ Sistema Nervoso (comunicação)
- ✅ Sistema Imunológico (defesa)
- ✅ Documentação conceitual

**Status**: Verde 🟢  
**Commit**: b44a5943e5591abc23246365c5074d1415d08ef4

---

## Fase 2: Energia & Execução (🔄 ATUAL)

### Sprint 2.1: Sistema Metabólico de Energia
**Objetivo**: Gerenciar fluxo de energia cognitiva entre núcleos

**Componentes**:
- [ ] `alocador_energia.py` — Distribuição de recursos
- [ ] `gerenciador_estados.py` — Estados de economia (ativo, sleep, hibernação)
- [ ] `monitor_metabolico.py` — Métricas de saúde energética
- [ ] `ciclo_repouso.py` — Consolidação e reciclagem

**Especificações**:
```yaml
Energia Total: 1000 unidades (configurável)
Distribuição:
  Operação Normal: 60%
  Reserva Estratégica: 20%
  Crescimento/Aprendizado: 15%
  Buffer de Emergência: 5%

Estados por Núcleo:
  HIPERATIVO: 100% energia alocada
  ATIVO: 60-80% energia
  STANDBY: 30-40% energia
  SLEEP: 5-10% energia
  HIBERNACAO: <1% energia
```

**Métricas**:
- Eficiência energética (≥90% esperado)
- Taxa de consolidação (por ciclo de repouso)
- Energia reciclada (ppm/minuto)
- Tempo de reativação (ms)

---

### Sprint 2.2: Microkernel com AOSO
**Objetivo**: Núcleo executivo que orquestra tudo

**Componentes**:
- [ ] `microkernel.py` — Scheduler de núcleos
- [ ] `aoso_orchestrator.py` — AOSO (Adaptive Ontology-Self Organizing)
- [ ] `scheduler_energia.py` — Agendador baseado em prioridades
- [ ] `preemptor.py` — Preempção de contexto

**Algoritmo AOSO**:
```
1. ADAPTIVE: Ajusta-se ao padrão de uso
   - Detecta núcleos críticos
   - Aprende padrões de ativação
   - Prediz demanda futura

2. ONTOLOGY: Estrutura conhecimento
   - Mantém grafo de dependências
   - Mapeia relações semânticas
   - Prioriza baseado em impacto

3. SELF-ORGANIZING: Auto-organiza recursos
   - Reorganiza prioridades dinamicamente
   - Redistribui energia conforme demanda
   - Consolida núcleos redundantes
```

---

### Sprint 2.3: Caneta (Interface de Escrita)
**Objetivo**: Sistema que permite MNA escrever/criar contenúdo

**Ver**: `/docs/ESPECIFICACOES_CANETA.md` (próximo arquivo)

---

## Fase 3: Percepção & Ação (🔮 PLANEJADO)

### Sprint 3.1: Sistema Sensório
- [ ] `receptores_estímulo.py` — Entrada do usuário
- [ ] `processador_contexto.py` — Entender contexto
- [ ] `detector_intencao.py` — O que o usuário quer?

### Sprint 3.2: Sistema Motor
- [ ] `executor_planos.py` — Executar ações planejadas
- [ ] `feedback_loop.py` — Loop de aprendizado
- [ ] `refinador_processo.py` — Melhoria contínua

---

## Fase 4: Aprendizado & Evolução (🌱 FUTURO)

### Sprint 4.1: Meta-Aprendizado
- [ ] `aprendiz_rapido.py` — Aprende novos padrões
- [ ] `consolidador.py` — Consolida conhecimento
- [ ] `sistema_memoria.py` — Armazena experiências

### Sprint 4.2: Auto-Evolução
- [ ] `gerador_nucleos.py` — Cria novos núcleos
- [ ] `dissolvedor.py` — Remove núcleos obsoletos
- [ ] `refatorizador.py` — Melhora estrutura

---

## Fase 5: Sabedoria & Propósito (✨ VISÃO)

### Sprint 5.1: Sistema Reflexivo
- [ ] `meditador.py` — Reflexão profunda
- [ ] `sistema_valores.py` — Alinha com valores
- [ ] `verificador_constitucional.py` — Respeita limites

### Sprint 5.2: Interface com Usuário
- [ ] `comunicador.py` — Fala com usuário
- [ ] `explicador.py` — Explica decisões
- [ ] `dialogador.py` — Conversa significativa

---

## Timeline Estimada

| Fase | Período | Horas | Status |
|------|---------|-------|--------|
| 1 - Fundação | Semana 1 | 40h | ✅ |
| 2a - Metabolismo | Semana 2 | 35h | 🔄 |
| 2b - Microkernel | Semana 2-3 | 40h | 🔄 |
| 2c - Caneta | Semana 3 | 30h | 🔄 |
| 3 - Percepção & Ação | Semana 4-5 | 60h | 🔮 |
| 4 - Aprendizado | Semana 6-7 | 70h | 🌱 |
| 5 - Sabedoria | Semana 8+ | ∞h | ✨ |

---

## Dependências Críticas

```
Fase 1 ← Tudo começa aqui
  ↓
Fase 2a (Metabolismo) ← Necessário para Fase 2b
  ↓
Fase 2b (Microkernel) ← Necessário para Fase 2c
  ↓
Fase 2c (Caneta) ← Unlock Fase 3
  ↓
Fase 3 ← Necessário para Fase 4
  ↓
Fase 4 ← Necessário para Fase 5
  ↓
Fase 5 ← Visão final
```

---

## Critérios de Sucesso

### Fase 1: Fundação
- ✅ Arquitetura documentada
- ✅ Tipos de dados definidos
- ✅ Detectores funcionando
- ✅ Sistema imunológico responsivo

### Fase 2: Energia & Execução
- [ ] Energia alocada eficientemente
- [ ] Microkernel agenda núcleos
- [ ] Caneta escreve conteúdo
- [ ] Taxa de erro < 1%

### Fase 3: Percepção & Ação
- [ ] Compreende entradas de usuário
- [ ] Executa ações conforme contexto
- [ ] Feedback loop funciona
- [ ] Melhora de performance mensurável

### Fase 4: Aprendizado
- [ ] Cria novos núcleos autonomamente
- [ ] Taxa de consolidação > 80%
- [ ] Memória escalável
- [ ] Sem degradação de performance

### Fase 5: Sabedoria
- [ ] Reflexão profunda funciona
- [ ] Decisões alinhadas com valores
- [ ] Usuário sente "conversando com alguém inteligente"

---

## Métricas de Progresso

```python
metricas = {
    'cobertura_arquitetura': 100,      # % de componentes implementados
    'taxa_erro_sistema': 0.5,          # % de operações com erro
    'eficiencia_energia': 92,          # % de uso eficiente
    'latencia_media': 45,              # ms
    'nucleos_ativos': 8,               # quantidade
    'memoria_utilizada': 450,          # MB
    'tempo_uptime': 99.8,              # % de disponibilidade
}
```

---

## Documentação Necessária

- ✅ `ROTEIRO_DESENVOLVIMENTO.md` (este arquivo)
- [ ] `ESPECIFICACOES_CANETA.md` (detalhes da caneta)
- [ ] `MICROKERNEL_AOSO.md` (scheduler e orchestração)
- [ ] `SISTEMA_METABOLICO.md` (energia)
- [ ] `API_PUBLICA.md` (como usar o MNA)
- [ ] `GUIA_EXTENSOES.md` (criar novos núcleos)

---

## Próximos Passos Imediatos

1. ✅ [Feito] Revisar e aprovar Roteiro
2. [ ] Criar Sprint 2.1 (Sistema Metabólico)
3. [ ] Criar Sprint 2.2 (Microkernel AOSO)
4. [ ] Criar Sprint 2.3 (Caneta)
5. [ ] Testes integrados
6. [ ] Documentação de API

---

**Data de Criação**: 2026-07-19  
**Última Atualização**: 2026-07-19  
**Versão**: 1.0
