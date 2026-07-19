# ⚙️ Microkernel com AOSO (Adaptive Ontology-Self Organizing)

## Visão Geral

O **Microkernel** é o "cérebro executivo" do MNA. Ele:
1. **Agenda** qual núcleo executa em cada momento
2. **Aloca** energia baseado em prioridades
3. **Monitora** saúde e performance
4. **Reorganiza** dinamicamente conforme demanda

```
┌─────────────────────────────────────────────┐
│         MICROKERNEL (Executor)              │
│  ┌───────────────────────────────────────┐  │
│  │  AOSO Orchestrator                    │  │
│  │  - Mantém Ontologia de Núcleos       │  │
│  │  - Auto-organiza prioridades         │  │
│  │  - Adapta-se a padrões              │  │
│  └───────────────┬───────────────────────┘  │
│                  │                          │
│    ┌─────────────┼─────────────┐           │
│    │             │             │           │
│    ↓             ↓             ↓           │
│  ┌────┐        ┌────┐        ┌────┐       │
│  │NME │        │NAS │        │NIE │       │
│  └────┘        └────┘        └────┘       │
│    │             │             │           │
│    │             │             │           │
│  ┌────┐        ┌────┐        ┌────┐       │
│  │NSM │        │Novo│        │Novo│       │
│  └────┘        └────┘        └────┘       │
└─────────────────────────────────────────────┘
      ↓
   Sistema Nervoso
   Sistema Metabólico
   Sistema Imunológico
```

---

## Algoritmo AOSO

### A - ADAPTIVE (Adaptativo)

**Função**: Ajustar-se ao padrão de uso observado

```
1. Observa ativação de núcleos ao longo do tempo
2. Detecta padrões: "NME sempre ativa quando user pergunta sobre passado"
3. Aprende previsões: "User vai perguntar X, logo NME deve acordar agora"
4. Ajusta alocação: Dá mais energia a NME antes que seja pedida
```

**Implementação**:
```python
class ComponenteAdaptativo:
    
    async def aprender_padroes(self):
        """Observa padrões de ativação de núcleos"""
        
        for timestamp, evento in self.historico_eventos:
            padrão = extrair_padrão(evento)
            if padrão.frequencia > limiar:
                self.padroes_conhecidos[padrão.id] = padrão
    
    async def prever_proxima_ativacao(self) -> List[str]:
        """Prediz quais núcleos serão ativados em breve"""
        
        nucleos_previstos = []
        contexto_atual = self.get_contexto()
        
        for padrao in self.padroes_conhecidos:
            if contexto_atual.matches(padrao.condicoes):
                nucleos_previstos.append(padrao.nucleo_ativado)
        
        return nucleos_previstos
```

**Exemplo**:
```
[14:00] User abre MNA
[14:05] NSM ativa (segurança)
[14:10] NME ativa (busca memória)
[14:15] NAS ativa (análise simbólica)
[14:20] Resposta gerada

└─ PADRÃO DETECTADO: Sequência NSM → NME → NAS
   Probabilidade: 87%
   
└─ PRÓXIMA VEZ User abre MNA:
   Microkernel "acorda" os 3 juntos
   Reduz latência de 1.5s para 0.5s
```

### O - ONTOLOGY (Ontologia)

**Função**: Manter estrutura de conhecimento dos núcleos

```
Ontologia = Grafo de Núcleos
  Nós: Núcleos do MNA
  Arestas: Relacionamentos
    - "NME depende de NAS" (o significado de uma memória precisa de análise)
    - "NSM pode vetar NME" (segurança pode bloquear ação)
    - "NIE coordena NAS+NME" (estrutura integra análise + memória)
```

**Matriz de Dependência**:
```
     NME  NAS  NIE  NSM
NME   -   3.0  0.5  1.0   (NME depende muito de NAS)
NAS   2.0  -   2.5  0.2   (NAS depende de NME e NIE)
NIE   0.3  1.5  -   0.1   (NIE coordena mas é independente)
NSM   1.0  1.0  1.0  -    (NSM afeta todos igualmente)
```

**Impacto de Prioridade**:
```
Se aumentar prioridade de NAS:
  └─ NIE recebe boost (depende de NAS)
  └─ NME recebe boost (trabalha com NAS)
  └─ NSM monitora (sempre atento)

Resultado: Decisão coerente com cascata eficiente
```

**Implementação**:
```python
class OntologiaNucleos:
    
    def __init__(self):
        self.grafo: DiGraph = DiGraph()  # Grafo direcionado
        self.pesos_dependencia: Dict = {}  # Força das relações
    
    def calcular_impacto_prioritario(self, nucleo: str) -> Dict[str, float]:
        """Calcula cascata de prioridade"""
        
        impactos = {}
        
        # BFS para encontrar dependentes
        for dependente in nx.descendants(self.grafo, nucleo):
            distancia = nx.shortest_path_length(self.grafo, nucleo, dependente)
            peso = self.pesos_dependencia.get((nucleo, dependente), 1.0)
            impacto = peso / (1 + distancia)  # Descontado por distância
            impactos[dependente] = impacto
        
        return impactos
    
    def otimizar_ordem_execucao(self, nucleos_ativos: List[str]) -> List[str]:
        """Ordena execução respeitando dependências"""
        
        # Topological sort com pesos
        try:
            ordem = list(nx.topological_sort(self.grafo.subgraph(nucleos_ativos)))
        except nx.NetworkXError:
            # Ciclo detectado - resolver
            ordem = self._resolver_ciclo(nucleos_ativos)
        
        return ordem
```

### SO - SELF-ORGANIZING (Auto-Organizável)

**Função**: Reorganizar dinamicamente sem comando central

```
1. Cada núcleo monitora sua performance
2. Comunica problemas ao microkernel
3. Microkernel descobre solução emergente
4. Sistema se reorganiza sem intervenção
```

**Exemplos**:

**Cenário 1: Sobrecarga**
```
NAS está 95% utilizado
  ↓
NAS sinala: "Posso falhar em 5 minutos"
  ↓
Microkernel recalcula
  ├─ Reduz outras tarefas de NAS
  ├─ Aumenta banda de NIE
  └─ Equilibra carga
```

**Cenário 2: Núcleo Bloqueado**
```
NME esperando dados de NAS
NAS esperando dados de NIE
NIE esperando dados de NME (deadlock!)
  ↓
Microkernel detecta ciclo
  ├─ Quebra um elo (coloca NIE em sleep)
  ├─ Deixa NME↔NAS convergirem
  └─ Reativa NIE com dados corretos
```

**Implementação**:
```python
class OrganizadorAutonomo:
    
    async def ciclo_auto_organizacao(self):
        """Executa constantemente para manter equilíbrio"""
        
        while True:
            # 1. Coleta métricas de todos os núcleos
            metricas = await self.coletar_metricas()
            
            # 2. Detecta problemas
            problemas = self.detectar_problemas(metricas)
            
            # 3. Propõe reorganização
            if problemas:
                nova_configuracao = self.propor_reorganizacao(problemas)
                
                # 4. Aplica gradualmente (sem quebrar nada)
                await self.aplicar_reorganizacao(nova_configuracao, gradual=True)
            
            # 5. Aguarda próximo ciclo
            await asyncio.sleep(100 / 1000)  # 100ms
    
    def detectar_problemas(self, metricas: Dict) -> List[str]:
        """Identifica gargalos e ineficiências"""
        
        problemas = []
        
        # Sobrecarga?
        for nucleo, metrica in metricas.items():
            if metrica['utilizacao'] > 0.90:
                problemas.append(f'sobrecarga_{nucleo}')
        
        # Deadlock?
        if self.detectar_deadlock(metricas):
            problemas.append('deadlock_detectado')
        
        # Latência alta?
        if metricas['latencia_media'] > 1000:
            problemas.append('latencia_critica')
        
        return problemas
```

---

## Scheduler de Energia

### Algoritmo CFS (Completely Fair Scheduler) Adaptado

```
Cada núcleo recebe "fatia de tempo" proporcional à sua prioridade

Prioridade = Base + Dinamica
  Base: Definida pelo usuário/constitução
  Dinâmica: Baseada em carga atual e padrões

Tempo Alocado = (Prioridade / Soma_Prioridades) × Tempo_Total
```

**Exemplo**:
```
Núcleos Ativos:
  NME: prioridade 5 (normal)
  NAS: prioridade 8 (elevada - processando texto pesado)
  NIE: prioridade 3 (baixa - standby)
  NSM: prioridade 10 (crítica - sempre)

Total de prioridade: 26
Tempo disponível: 1000ms

Distribuição:
  NME: (5/26) × 1000 = 192ms
  NAS: (8/26) × 1000 = 308ms
  NIE: (3/26) × 1000 = 115ms
  NSM: (10/26) × 1000 = 385ms
```

**Implementação**:
```python
class SchedulerEnergia:
    
    def calcular_distribuicao(self, nucleos: Dict[str, int]) -> Dict[str, int]:
        """Calcula quanto tempo cada núcleo recebe"""
        
        prioridades = {nid: n.prioridade for nid, n in nucleos.items()}
        soma_prioridades = sum(prioridades.values())
        
        tempo_total = 1000  # 1 segundo
        distribuicao = {}
        
        for nucleo_id, prioridade in prioridades.items():
            tempo = int((prioridade / soma_prioridades) * tempo_total)
            distribuicao[nucleo_id] = tempo
        
        return distribuicao
    
    async def executar_pulso(self, nucleos: Dict):
        """Executa um pulso de energia com distribuição justa"""
        
        distribuicao = self.calcular_distribuicao(nucleos)
        
        for nucleo_id, tempo_ms in distribuicao.items():
            nucleo = nucleos[nucleo_id]
            
            # Executa com timeout
            try:
                await asyncio.wait_for(
                    nucleo.executar(),
                    timeout=tempo_ms / 1000
                )
            except asyncio.TimeoutError:
                logger.warning(f"{nucleo_id} excedeu tempo alocado")
                # Núcleo continua, mas perde prioridade próxima vez
```

---

## Preempção e Context Switch

### Quando Fazer Preempção?

```
1. TEMPORAL: Núcleo excedeu seu quantum (fatia de tempo)
2. PRIORIDADE: Novo evento de alta prioridade chega
3. SEGURANÇA: NSM necessita verificação imediata
4. EMERGÊNCIA: Sistema detecta falha iminente
```

**Implementação**:
```python
class Preemptor:
    
    async def verificar_preempcao(self):
        """Verifica se deve fazer preempção"""
        
        nucleo_atual = self.nucleos_em_execucao[-1]
        tempo_decorrido = time.time() - nucleo_atual.tempo_inicio
        quantum_alocado = nucleos[nucleo_atual.id].quantum_ms
        
        # Condição 1: Tempo esgotado?
        if tempo_decorrido * 1000 > quantum_alocado:
            return True
        
        # Condição 2: Evento de alta prioridade?
        if self.fila_eventos and self.fila_eventos[0].prioridade > 8:
            return True
        
        # Condição 3: NSM precisa?
        if self.nsm.necessita_intervencao():
            return True
        
        return False
    
    async def fazer_context_switch(self, novo_nucleo_id: str):
        """Troca contexto de execução"""
        
        nucleo_anterior = self.nucleos_em_execucao[-1]
        
        # 1. Salva estado
        contexto_salvo = await nucleo_anterior.salvar_contexto()
        
        # 2. Restaura novo contexto
        novo_nucleo = self.nucleos[novo_nucleo_id]
        await novo_nucleo.restaurar_contexto()
        
        # 3. Troca na fila
        self.nucleos_em_execucao.pop()
        self.nucleos_em_execucao.append(novo_nucleo)
        
        logger.debug(f"Context switch: {nucleo_anterior.id} → {novo_nucleo_id}")
```

---

## Monitoramento e Observabilidade

### Métricas Coletadas

```python
metricas_microkernel = {
    'cpu_utilization': 0-100,           # % uso total
    'context_switches_per_sec': int,    # frequência de troca
    'average_latency': float,           # ms médio
    'queue_depth': int,                 # eventos aguardando
    'scheduling_efficiency': 0-1.0,     # quão bem usa tempo
    'preemptions_per_sec': int,         # quantas vezes interrompe
    'deadlock_detections': int,         # ciclos encontrados
}
```

### Dashboard de Monitoramento

```
┌─────────────────────────────────────────┐
│   MICROKERNEL STATUS                    │
├─────────────────────────────────────────┤
│                                         │
│  CPU: ████████░░ 82%                   │
│                                         │
│  Núcleos Ativos:                        │
│    NME: ██████░░░░ 60%                  │
│    NAS: ████████░░ 80%                  │
│    NIE: ███░░░░░░░ 30%                  │
│    NSM: ██████████ 100%                 │
│                                         │
│  Eventos na Fila: 12                    │
│  Context Switches: 234/sec              │
│  Latência Média: 45ms                   │
│  Eficiência: 94%                        │
│                                         │
│  ⚠️ NSM: Verificação de segurança       │
│  ✓ Todos os núcleos saudáveis           │
│                                         │
└─────────────────────────────────────────┘
```

---

## Exemplos de Execução

### Exemplo 1: Início de Conversa Normal

```
T=0ms:   User abre MNA
T=10ms:  NSM acorda (segurança)
T=50ms:  NAS acorda (análise)
T=100ms: NME preparando contexto
T=150ms: NIE coordenando
T=200ms: Sistema pronto
T=300ms: Resposta começa a ser gerada
```

### Exemplo 2: Alerta de Segurança

```
T=0ms:   NAS processando requisição
T=100ms: Detector encontra padrão suspeito
T=105ms: PREEMPÇÃO: NAS é interrompido
T=110ms: NSM é ativado em máxima prioridade
T=150ms: NSM verifica e bloqueia
T=160ms: NAS resume de onde parou
```

### Exemplo 3: Deadlock e Recuperação

```
T=0ms:   NME esperando dados de NAS
T=100ms: NAS esperando dados de NIE
T=150ms: NIE esperando dados de NME ⚠️
         DEADLOCK DETECTADO
T=160ms: PREEMPÇÃO: NIE congelado
T=170ms: NAS obtém dados alternativos
T=180ms: NME continua
T=190ms: NIE reativado com dados corretos
T=200ms: Sistema normaliza
```

---

## Testes de Validação

```python
async def testar_microkernel():
    
    # Teste 1: Distribuição justa
    assert scheduler.calcular_distribuicao({...}) == esperado
    
    # Teste 2: Preempção
    await preemptor.fazer_context_switch(novo_id)
    assert nucleos[novo_id].ativo == True
    
    # Teste 3: Detecção de deadlock
    criar_ciclo(NME, NAS, NIE)
    await organizador.detectar_deadlock()
    assert problemas_detectados > 0
    
    # Teste 4: Performance
    latencia = await medir_latencia_media()
    assert latencia < 100  # ms
    
    # Teste 5: Adaptação
    await observar_padroes(1000 iterações)
    previsoes = adaptador.prever_proxima_ativacao()
    assert acuracidade_predicoes > 0.80
```

---

**Status**: 🟡 Especificação Completa - Pronto para Implementação  
**Versão**: 1.0  
**Data**: 2026-07-19
