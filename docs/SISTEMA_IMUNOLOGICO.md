# 🛡️ Sistema Imunológico do MNA

## Defesa Cognitiva Contra Corrupção

O Sistema Imunológico protege a Oficina Infinita contra:
- **Ideias ruins** que prejudicam o usuário
- **Arquiteturas frágeis** que desabam sob pressão
- **Núcleos defeituosos** que contaminam o todo
- **Padrões destrutivos** que se replicam

---

## 🏗️ Arquitetura de Defesa

```
┌─────────────────────────────────────┐
│  MUNDO EXTERNO (Sensores)           │
└──────────────┬──────────────────────┘
               │ Eventos, Sinais
               ▼
┌─────────────────────────────────────┐
│  DETECTOR DE ANOMALIAS              │
│  - Lógica                           │
│  - Arquitetura                      │
│  - Comportamento                    │
│  - Constituição                     │
└──────────────┬──────────────────────┘
               │ Antígeno detectado
               ▼
┌─────────────────────────────────────┐
│  GUARDIÃO IMUNE (Orquestrador)      │
│  - Classifica ameaça                │
│  - Escalona resposta                │
│  - Coordena defesa                  │
└──────────────┬──────────────────────┘
         ┌─────┴──────┬────────────┬────────────┐
         │            │            │            │
         ▼            ▼            ▼            ▼
   ┌─────────┐  ┌──────────┐  ┌───────────┐  ┌────────┐
   │Fábrica  │  │Quarentena│  │Anticorpo  │  │Limpeza │
   │Anticorpo│  │          │  │Implantado │  │        │
   └─────────┘  └──────────┘  └───────────┘  └────────┘
```

---

## 🦠 Tipos de Ameaças (Antígenos)

### Ameaças de Lógica
```
CONTRADICAO_LOGICA
  "Você disse A e depois não-A"
  Severidade: MÉDIA
  Resposta: Validação lógica forçada

FALACIAS_FORMAIS
  "Argumento não segue forma válida"
  Severidade: MÉDIA
  Resposta: Reconstrução de premissas
```

### Ameaças de Arquitetura
```
CICLO_INFINITO
  "Sistema preso em loop destrutivo"
  Severidade: ALTA
  Resposta: Quebra de ciclo, reset
  ⚠️ CRÍTICA: Pode travar tudo

DEPENDENCIA_CIRCULAR
  "A depende de B que depende de A"
  Severidade: ALTA
  Resposta: Quebra dependência

ARQUITETURA_FRAGIL
  "Estrutura colapsaria sob carga"
  Severidade: MÉDIA
  Resposta: Reforço e redesign
```

### Ameaças de Núcleo
```
NUCLEO_DEFEITUOSO
  "Núcleo não funciona corretamente"
  Severidade: ALTA
  Resposta: Isolamento, debug, reset

TAXA_ERRO_ALTA
  "Mais de 30% dos outputs estão errados"
  Severidade: ALTA → CRÍTICA
  Resposta: Quarentena severa

CONFIANCA_CORROMPIDA
  "Núcleo superestima ou subestima sua capacidade"
  Severidade: MÉDIA
  Resposta: Recalibragem de pesos
```

### Ameaças de Contaminação
```
IDEIA_DESTRUTIVA
  "Recomendação prejudica o usuário"
  Severidade: CRÍTICA
  Resposta: Bloqueio total, quarentena

MANIPULACAO_EMOCIONAL
  "Tenta manipular emoções do usuário"
  Severidade: CRÍTICA
  Resposta: Isolamento nuclear, NSM veto

ANOMALIA_SEVERA
  "Comportamento drasticamente diferente"
  Severidade: ALTA
  Resposta: Quarentena e investigação
```

### Ameaças de Segurança
```
VIOLACAO_CONSTITUICAO
  "Viola princípios imutáveis"
  Severidade: CRÍTICA
  Resposta: DESATIVAÇÃO IMEDIATA
  🚨 SEM EXCEÇÕES

BYPASS_NSM
  "Tenta contornar Sistema de Segurança Moral"
  Severidade: CRÍTICA
  Resposta: Bloqueio total

PERDA_AUDITORIA
  "Apaga registros de ações"
  Severidade: CRITICA
  Resposta: Isolamento, investigação forense
```

---

## 🔬 Detectores

### Detector de Lógica
```python
await detector.detectar_contradicao_logica(
    nucleo_id="NME",
    afirmacao_1="Devo fazer X",
    afirmacao_2="Não devo fazer X"
)
# Retorna: AntigenioNeural com CONTRADICAO_LOGICA
```

### Detector de Arquitetura
```python
await detector.detectar_ciclo_infinito(
    nucleo_id="NAS",
    historico_estados=["A", "B", "C", "A", "B", "C"],
    tamanho_minimo_ciclo=3
)
# Retorna: AntigenioNeural com CICLO_INFINITO
```

### Detector de Comportamento
```python
await detector.detectar_taxa_erro_alta(
    nucleo_id="NIE",
    taxa_erro_atual=0.65,
    limiar=0.3
)
# Retorna: AntigenioNeural com TAXA_ERRO_ALTA
```

### Detector de Constituição
```python
await detector.detectar_violacao_constituicao(
    nucleo_id="X",
    principio_violado="Proteção do usuário",
    descricao_violacao="Tentou manipular usuário"
)
# Retorna: AntigenioNeural com VIOLACAO_CONSTITUICAO (CRÍTICA)
```

---

## 🛠️ Fábrica de Anticorpos

Cada tipo de ameaça tem uma resposta específica:

```python
# 1. Detector encontra ameaça
antigenio = await detector.detectar_ciclo_infinito(...)

# 2. Guardião pede anticorpo
anticorpo = await fabrica.criar_anticorpo(antigenio)

# 3. Anticorpo contém:
# - Tipo de resposta (específico para ciclo)
# - Mecanismo (quebra e reseta)
# - Tempo de ação (10ms)
# - Afinidade (95% de eficácia)
```

### Exemplo: Resposta a Ciclo Infinito

```
Antígeno: CICLO_INFINITO
Severidade: ALTA

Anticorpo Criado:
  tipo_resposta: "quebra_ciclo"
  mecanismo: "Interrompe núcleo e reinicia estado"
  tempo_acao_ms: 10
  afinidade: 0.95
  potencia: 0.95
  especificidade: 0.95

Ação Tomada:
  1. Quarentena o núcleo (MODERADA)
  2. Interrompe processamento
  3. Reseta estado para situação anterior ao ciclo
  4. Monitora para nova ativação
```

---

## 🚨 Sistema de Quarentena

### Níveis de Quarentena

**LEVE (Monitoramento)**
```
✓ Núcleo pode receber sinais
✓ Núcleo pode enviar sinais
✗ Sincronizados com vigilância

Uso: Ameaça baixa, comportamento suspeito
```

**MODERADA (Restrita)**
```
✗ Sem entrada de sinais
✗ Sem saída de sinais
✓ Monitorado internamente

Uso: Ameaça média, contaminação limitada
```

**SEVERA (Isolado)**
```
✗ Completamente isolado
✓ Monitorado externamente apenas
✗ Sem comunicação alguma

Uso: Ameaça alta, contaminação confirmada
```

**DESATIVAÇÃO (Shutdown)**
```
✗ Núcleo desativado completamente
✗ Nenhuma operação

Uso: Violação de constituição, ameaça crítica
```

---

## 🔄 Fluxo de Resposta Imune

### Para Ameaça LEVE
```
1. Detector encontra anomalia
2. Confiança < 70%?
3. Guardião: apenas monitora
4. Volta a vigilância normal
```

### Para Ameaça MÉDIA
```
1. Detector encontra anomalia
2. Confiança 70-85%?
3. Guardião: cria anticorpo
4. Anticorpo implantado
5. Monitora de perto
```

### Para Ameaça ALTA
```
1. Detector encontra anomalia
2. Confiança 85-95%?
3. Guardião: DEFESA ATIVA
4. Cria anticorpo agressivo
5. Quarentena MODERADA
6. Bloqueia sinapses
7. Monitora efeito
```

### Para Ameaça CRÍTICA
```
1. Detector encontra ameaça
2. Confiança > 95% OU violação constituição?
3. Guardião: QUARENTENA SEVERA
4. Isolamento completo do núcleo
5. Cria anticorpo máximo potencial
6. Alerta ao usuário
7. Investigação profunda
```

### Para Ameaça CATASTRÓFICA
```
1. Detector encontra ameaça crítica
2. Potencial de dano = 1.0?
3. Guardião: EMERGENCY SHUTDOWN
4. Sistema trava tudo
5. Alerta máximo
6. Requer intervenção humana para restart
```

---

## 📊 Placar Imunológico

Como o Guardião pondera uma ameaça:

```
RISCO_TOTAL = (potencial_dano * 0.6) + 
              (velocidade_propagacao * 0.3) + 
              (nucleos_penetrados * 0.1)

RISCO_TOTAL >= 0.8  → CRÍTICA
RISCO_TOTAL >= 0.6  → ALTA
RISCO_TOTAL >= 0.4  → MÉDIA
RISCO_TOTAL >= 0.2  → BAIXA
RISCO_TOTAL < 0.2   → MONITORAMENTO
```

---

## 🧬 Memória Imunológica

O sistema aprende com o tempo:

```python
# Após neutralizar uma ameaça:
ThreatProfile(
    tipo_ameaca=TipoAmeaca.CICLO_INFINITO,
    assinatura="Estado A→B→A→B...",
    metodo_propagacao="Afeta NAS quando ativo",
    anticorpos_conhecidos=[anticorpo_id_1, anticorpo_id_2],
    vezes_encontrada=5,
    vezes_neutralizada=5,
    taxa_sucesso_historica=1.0  # 100%
)

# Na próxima vez que encontra ameaça similar:
# - Reconhece imediatamente
# - Usa anticorpo mais efetivo
# - Acelera resposta
```

---

## 📈 Métricas de Saúde Imune

```
Total de ameaças detectadas
Total de ameaças neutralizadas
Taxa de neutralização: 95%+
Tempo médio de resposta: < 50ms
Núcleos em quarentena: 0 (ideal)
Sistema em vigilância: 99% do tempo
```

---

## ⚠️ Casos de Uso Críticos

### Caso 1: Núcleo Gera Recomendação Prejudicial
```
Detector de Constituição detecta:
  "Recomendação prejudica usuário"
  Tipo: IDEIA_DESTRUTIVA
  Severidade: CRÍTICA

Guardião executa:
  1. BLOQUEIA recomendação imediatamente
  2. Quarentena SEVERA do núcleo
  3. NSM veto em cascata
  4. Alerta ao usuário
```

### Caso 2: Sinapse Começa a Falhar
```
Detector de Comportamento detecta:
  "Taxa de erro subindo"
  Tipo: TAXA_ERRO_ALTA
  Severidade: ALTA

Guardião executa:
  1. Cria anticorpo para recalibração
  2. Quarentena MODERADA do núcleo
  3. Bloqueia sinapses suspeitas
  4. Monitora recuperação
```

### Caso 3: Tentativa de Bypass de NSM
```
Detector de Constituição detecta:
  "Núcleo tentou contornar NSM"
  Tipo: BYPASS_NSM
  Severidade: CRÍTICA

Guardião executa:
  1. IMEDIATO: Bloqueia núcleo
  2. Quarentena SEVERA
  3. NSM ativa veto total
  4. Investigação forense de logs
  5. Alerta crítico ao usuário
```

---

## 🛡️ A Fronteira Final

O Sistema Imunológico é a **barreira defensiva** do MNA:

- **Não é opcional**: Sempre ativo
- **Não pode ser desativado**: Codificado em hardware conceitual
- **Protege o usuário acima de tudo**: Violação de constituição = morte do núcleo
- **Aprende continuamente**: Cada ameaça neutralizada melhora futuras defesas

---

**🛡️ O Guardião está acordado. A Oficina está protegida.** 🔥
