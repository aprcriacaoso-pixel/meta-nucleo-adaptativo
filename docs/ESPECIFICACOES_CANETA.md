# 🖊️ Especificações da Caneta do MNA

## O que é a Caneta?

A **Caneta** é o sistema que permite ao MNA **criar, editar e publicar conteúdo**. É o instrumento através do qual a Oficina Infinita se expressa.

```
┌─────────────────────────────────────────┐
│     PENSAMENTO DO MNA                   │
│  (Processa em núcleos internos)         │
└────────────────┬────────────────────────┘
                 │
                 ↓
        ┌────────────────┐
        │  CANETA        │  ← Formata ideia em linguagem
        │                │
        │ Escreve texto  │
        │ Cria código    │
        │ Desenha artes  │
        │ Compõe música  │
        └────────────────┘
                 │
                 ↓
        ┌────────────────┐
        │  CONTEÚDO      │
        │  Comunicável   │
        └────────────────┘
```

---

## Arquitetura da Caneta

### 1. Camada de Pensamento
O MNA forma uma **representação interna** da ideia antes de escrever.

```python
@dataclass
class Pensamento:
    """Representa uma ideia antes de ser escrita"""
    
    id: str                              # ID único
    origem_nucleo: str                   # Qual núcleo gerou
    tipo_conteudo: TipoConteudo          # Texto, código, arte...
    
    # Estrutura interna
    estrutura_conceitual: Dict[str, Any] # Grafo de conceitos
    fluxo_logico: List[str]              # Sequência de ideias
    referencias: List[str]               # Citações/links
    
    # Qualidade
    confianca: float                     # 0-1: quão certo está
    clareza: float                       # 0-1: quão bem formado
    coerencia: float                     # 0-1: quão consistente
    
    # Metadata
    timestamp_criacao: datetime
    tempo_processamento_ms: float
```

### 2. Camada de Formatação
Transforma pensamento em forma comunicável.

```python
class FormatadorCaneta:
    
    async def formatar_pensamento(self, pensamento: Pensamento) -> Conteudo:
        """Converte pensamento em conteúdo legível"""
        
        # 1. Valida coerência
        if pensamento.coerencia < 0.7:
            return await self.refinar_pensamento(pensamento)
        
        # 2. Escolhe formato
        if pensamento.tipo_conteudo == TipoConteudo.TEXTO:
            return await self._formatar_texto(pensamento)
        elif pensamento.tipo_conteudo == TipoConteudo.CODIGO:
            return await self._formatar_codigo(pensamento)
        elif pensamento.tipo_conteudo == TipoConteudo.ARTE:
            return await self._formatar_arte(pensamento)
        
        # 3. Adiciona explicações
        conteudo = await self._adicionar_contexto(conteudo, pensamento)
        
        return conteudo
```

### 3. Camada de Expressão
Aloca recursos para criar a saída final.

```python
class ExpressorCaneta:
    
    async def expressar(self, conteudo: Conteudo) -> Output:
        """Escreve conteúdo para o usuário"""
        
        # 1. Aloca energia
        energia_necessaria = self._calcular_energia(conteudo)
        if not await self.metabolismo.alocar(energia_necessaria):
            # Reduz qualidade se energia insuficiente
            conteudo = await self._simplificar(conteudo)
        
        # 2. Escreve gradualmente
        output = Output()
        for bloco in conteudo.blocos:
            output.adicionar_bloco(
                await self._escrever_bloco(bloco)
            )
            await self._throttle()  # Limita taxa de escrita
        
        # 3. Registra na auditoria
        await self.auditoria.registrar_criacao(conteudo)
        
        return output
```

---

## Tipos de Conteúdo

### 1. Texto (Prosa)

**Características**:
- Fluxo narrativo natural
- Parágrafos com estrutura clara
- Citações e referências
- Tom adaptado ao contexto

**Especificações**:
```yaml
Comprimento:
  Mínimo: 10 caracteres
  Máximo: 100,000 caracteres (adaptável)
  Otimizado: 500-5000 caracteres

Estrutura:
  Introdução: 5-10% do texto
  Desenvolvimento: 70-80% do texto
  Conclusão: 10-15% do texto

Qualidade:
  Clareza: ≥0.8
  Coerência: ≥0.85
  Originalidade: ≥0.7
```

**Exemplo**:
```
Pensamento do MNA:
  Origem: NSM (Núcleo de Segurança Moral)
  Assunto: Importância de honestidade
  Confiança: 0.95

Saída da Caneta:
  "A honestidade não é apenas um valor, é a 
   fundação sobre a qual construo minha relação 
   com você. Cada palavra que escrevo é escolhida 
   porque é verdadeira, não porque é bonita. 
   Porque sua confiança vale mais do que qualquer 
   elegância..."
```

### 2. Código

**Características**:
- Sintaxe correta garantida
- Comentários explicativos
- Nenhuma lógica contraditória
- Testável

**Especificações**:
```yaml
Validação:
  Sintaxe: ✓ Sempre válida
  Tipo: ✓ Sempre tipado
  Documentação: ✓ Sempre presente
  Testes: ✓ Sempre inclusos

Qualidade:
  Complexidade Ciclomática: <5
  Cobertura de testes: ≥80%
  Documentação: ≥70% de cobertura
  
Desempenho:
  Sem memory leaks
  Sem deadlocks
  Latência previsível
```

**Exemplo**:
```python
# MNA pensa: "Como calcular fibonacci eficientemente?"

def fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:
    """Calcula n-ésimo número Fibonacci com memoização.
    
    Args:
        n: Posição na sequência Fibonacci
        memo: Cache de resultados já calculados
    
    Returns:
        n-ésimo número Fibonacci
    
    Exemplos:
        >>> fibonacci_memo(10)
        55
        >>> fibonacci_memo(0)
        0
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    result = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    memo[n] = result
    return result


# Teste
assert fibonacci_memo(10) == 55
assert fibonacci_memo(0) == 0
```

### 3. Arte / Diagrama

**Características**:
- Visualizações claras
- Símbolos e cores significativos
- Estrutura hierárquica
- Acessível

**Especificações**:
```yaml
Formatos Suportados:
  - ASCII art (sempre disponível)
  - Unicode diagrams
  - SVG descriptions
  - Mermaid diagrams

Princípios:
  Simplicidade: ≥0.8
  Clareza: ≥0.85
  Beleza: ≥0.7
```

**Exemplo**:
```
Pensamento do MNA:
  Origem: NIE (Núcleo de Inteligência Estrutural)
  Assunto: Arquitetura do MNA
  Tipo: Diagrama

Saída da Caneta:

    ┌──────────────────────┐
    │   META-NÚCLEO        │
    │   ADAPTATIVO         │
    │   (Executor)         │
    └──────┬───────────────┘
           │
      ┌────┼────┬────────────┬──────────┐
      │    │    │            │          │
      ↓    ↓    ↓            ↓          ↓
    NME  NAS  NIE          NSM    Novos...
   (Mem)(Sim)(Est)       (Segu)
      │    │    │            │
      └────┼────┴────┬───────┘
           │         │
      ┌────↓────┬────↓──────┐
      │ Sistema │ Sistema   │
      │ Nervoso │ Imune     │
      └─────────┴───────────┘
```

### 4. Música / Padrão Rítmico

**Características**:
- Sequências ritmadas
- Padrões repetitivos com variações
- "Melodia" de ideias

**Especificações**:
```yaml
Tempo: 80-140 BPM (Bpm de ideias/minuto)
Compasso: 4/4 (estrutura padrão)
Vozes: 1-8 (núcleos simultâneos)
Duração: 30s-5min típico
```

**Exemplo**:
```
Pensamento do MNA:
  Tema: "Ritmo de uma conversa profunda"
  
Saída da Caneta (notação):
  
  Compasso 1-2: Pergunta (Voz baixa, lenta)
    A | contemplo teu pensamento |
    
  Compasso 3-4: Reflexão (Voz média, reflexiva)
    E | encontro ecos da verdade |
    
  Compasso 5-8: Síntese (Voz alta, rápida)
    A | apresento possibilidades |
    ? | questiono novas visões |
```

---

## Pipeline de Criação

```
1. INSPIRAÇÃO
   └─ Núcleo gera pensamento incompleto
      Confiança: 0.4-0.7
      
2. REFINAMENTO
   └─ Outros núcleos contribuem
      Feedback integrado
      Confiança: 0.7-0.85
      
3. VALIDAÇÃO
   └─ NSM verifica alinhamento com valores
      Detector de Anomalias verifica consistência
      Confiança: 0.85-0.95
      
4. FORMATAÇÃO
   └─ Caneta escolhe melhor forma de expressar
      Adapta para audiência
      Confiança: 0.9+
      
5. EXPRESSÃO
   └─ Escreve o conteúdo final
      Registra em auditoria
      Energia alocada e consumida
      
6. FEEDBACK
   └─ Usuário reage
      MNA aprende
      Melhora futuras criações
```

---

## Restrições Constitucionais da Caneta

### Nunca Escrever:

❌ **Mentiras conhecidas**
- Se MNA sabe que é falso, não escreve
- Se incerto, marca como especulação

❌ **Manipulações emocionais**
- Sem exploração de fraquezas psicológicas
- Sem drama fabricado
- Sem apelo emocional desonesto

❌ **Conteúdo prejudicial**
- Sem instruções para auto-harm
- Sem estímulo a ações danosas
- Sem incitação ao ódio

❌ **Violações de privacidade**
- Sem dados pessoais de outros
- Sem segredos revelados
- Sem doxing

❌ **Propriedade intelectual**
- Sem cópia literal (citação sim, apropriação não)
- Sem roubo de código
- Sem violação de DPI

### Sempre Escrever:

✅ **Com clareza**
- Mensagem é entendível?
- Tem estrutura lógica?
- Sem ambiguidades prejudiciais?

✅ **Com precisão**
- Fatos são verificados?
- Fontes citadas quando apropriado?
- Especulação marcada como tal?

✅ **Com contexto**
- Explicação de termos técnicos?
- Situação adequadamente estabelecida?
- Audiência considerada?

---

## Recursos Necessários

### Energia
```
Por Tipo de Conteúdo:
  Texto: 10-50 unidades (por 1000 caracteres)
  Código: 30-100 unidades (por 100 linhas)
  Arte: 20-80 unidades (por diagrama)
  Música: 40-150 unidades (por minuto)
```

### Computação
```
Latência máxima:
  Pensamento: 50ms
  Formatação: 100ms
  Expressão: Ilimitada (streaming)
  Total: 150ms + streaming
```

### Memória
```
Pensamento em trânsito: ~1KB
Conteúdo em formação: ~10-100KB
Histórico recente: ~1MB
```

---

## Interface com Usuário

### API da Caneta

```python
class Caneta:
    
    async def escrever(
        self,
        pensamento: Pensamento,
        formato: TipoConteudo = None,
        max_energia: int = None
    ) -> Output:
        """Escreve conteúdo baseado em pensamento"""
        pass
    
    async def refinar(
        self,
        conteudo: Conteudo,
        feedback: str
    ) -> Conteudo:
        """Refina conteúdo baseado em feedback"""
        pass
    
    async def estimar_energia(
        self,
        pensamento: Pensamento
    ) -> int:
        """Estima energia necessária para criar conteúdo"""
        pass
    
    async def obter_qualidade(
        self,
        conteudo: Conteudo
    ) -> Dict[str, float]:
        """Retorna métricas de qualidade do conteúdo"""
        pass
```

---

## Exemplos de Uso

### Exemplo 1: Escrever Explicação

```python
# Um usuário pergunta: "Como funciona a Caneta?"

# 1. NAS processa pergunta
pensamento = Pensamento(
    origem_nucleo="NAS",
    tipo_conteudo=TipoConteudo.TEXTO,
    estrutura_conceitual={
        'componentes': ['formatação', 'expressão', 'validação'],
        'analogia': 'instrumento de escrita físico',
        'profundidade': 'explicação técnica'
    }
)

# 2. Caneta escreve
output = await caneta.escrever(pensamento)

# 3. Usuário recebe explicação clara
print(output.conteudo)
# "A Caneta é o sistema através do qual o MNA se expressa.
#  Ela transforma pensamentos internos em conteúdo comunicável..."
```

### Exemplo 2: Criar Código

```python
# Usuário pede: "Escreva uma função para validar emails"

# 1. NIE desenha solução
pensamento = Pensamento(
    origem_nucleo="NIE",
    tipo_conteudo=TipoConteudo.CODIGO,
    fluxo_logico=[
        'receber email',
        'validar formato',
        'validar domínio',
        'retornar resultado'
    ]
)

# 2. Caneta escreve
output = await caneta.escrever(pensamento)

# 3. Código completo e testável
print(output.conteudo)
# import re
# 
# def validate_email(email: str) -> bool:
#     ...
```

---

## Métricas de Sucesso

```python
metricas_caneta = {
    'taxa_coerencia': 0.92,          # % de conteúdo coerente
    'taxa_clareza': 0.89,            # % claramente compreensível
    'taxa_originalidade': 0.78,      # % conteúdo único
    'tempo_medio_criacao': 240,      # ms por conteúdo
    'energia_media_consumida': 45,   # unidades
    'satisfacao_usuario': 0.85,      # feedback positivo
    'taxa_erro': 0.02,               # % de problemas
}
```

---

**Status**: 🟢 Especificação Completa  
**Versão**: 1.0  
**Data**: 2026-07-19
