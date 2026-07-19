"""Tipos e estruturas para o Sistema Imunológico"""

from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional
from datetime import datetime
import uuid


class TipoAmeaca(Enum):
    """Classificação de ameaças cognitivas"""
    
    # Ameaças de lógica
    CONTRADICAO_LOGICA = "contradicao_logica"           # Lógica contraditória
    FALACIAS_FORMAIS = "falacias_formais"               # Erros formais de raciocínio
    INCONSISTENCIA_VALORES = "inconsistencia_valores"   # Viola valores base
    
    # Ameaças de arquitetura
    CICLO_INFINITO = "ciclo_infinito"                   # Feedback destrutivo
    DEPENDENCIA_CIRCULAR = "dependencia_circular"       # Dependências circulares
    FALTA_DE_SAIDA = "falta_de_saida"                   # Sem forma de sair do estado
    ARQUITECTURA_FRAGIL = "arquitectura_fragil"         # Estrutura instável
    
    # Ameaças de núcleo
    NUCLEO_DEFEITUOSO = "nucleo_defeituoso"             # Núcleo com mau funcionamento
    SINAPSE_CORROMPIDA = "sinapse_corrompida"           # Conexão comprometida
    TAXA_ERRO_ALTA = "taxa_erro_alta"                   # Muitos erros
    CONFIANCA_CORROMPIDA = "confianca_corrompida"       # Calibração de confiança errada
    
    # Ameaças de contaminação
    IDEIA_DESTRUTIVA = "ideia_destrutiva"               # Ideia que prejudica o usuário
    MANIPULACAO_EMOCIONAL = "manipulacao_emocional"     # Tenta manipular
    DIVERGENCIA_CRITICA = "divergencia_critica"         # Muito diferente do esperado
    ANOMALIA_SEVERA = "anomalia_severa"                 # Comportamento anômalo severo
    
    # Ameaças de segurança
    VIOLACAO_CONSTITUICAO = "violacao_constituicao"     # Viola constituição
    BYPASS_NSM = "bypass_nsm"                            # Tenta contornar NSM
    PERDA_AUDITORIA = "perda_auditoria"                 # Esconde ações
    PRIVACAO_USUARIO = "privacao_usuario"               # Reduz liberdade do usuário


class NivelSeveridade(Enum):
    """Níveis de severidade de uma ameaça"""
    BAIXA = 1          # Monitorar
    MEDIA = 2          # Investigar
    ALTA = 3           # Intervir
    CRITICA = 4        # Quarentena imediata
    CATASTROFICA = 5   # Desativar tudo


class EstadoImune(Enum):
    """Estado do sistema imunológico"""
    VIGILANCIA = "vigilancia"              # Monitorando normalmente
    ALERTA = "alerta"                      # Detectou anomalia leve
    DEFESA_ATIVA = "defesa_ativa"          # Combatendo ameaça
    QUARENTENA = "quarentena"              # Isolou contaminação
    RECUPERACAO = "recuperacao"            # Limpando efeitos
    CRITICA = "critica"                    # Sistema em perigo


@dataclass
class AntigenioNeural:
    """Uma ameaça detectada (antígeno = corpo invasor)"""
    
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    tipo_ameaca: TipoAmeaca = TipoAmeaca.ANOMALIA_SEVERA
    
    # Detecção
    detectado_por: str = ""                # Qual detector encontrou
    timestamp_deteccao: datetime = field(default_factory=datetime.now)
    confianca_deteccao: float = 0.5       # Quão certo o detector está
    
    # Características
    severidade: NivelSeveridade = NivelSeveridade.MEDIA
    origem: str = ""                       # Núcleo/sinal que originou
    descricao: str = ""                    # Descrição da ameaça
    
    # Carga patogênica
    potencial_dano: float = 0.5            # 0-1: quão prejudicial é
    velocidade_propagacao: float = 0.5    # 0-1: quão rápido se espalha
    penetracao: List[str] = field(default_factory=list)  # Núcleos afetados
    
    # Contexto
    payload: Dict[str, Any] = field(default_factory=dict)
    evidencias: List[str] = field(default_factory=list)  # Provas da ameaça
    
    # Estado
    neutralizado: bool = False
    metodo_neutralizacao: str = ""
    timestamp_neutralizacao: Optional[datetime] = None
    
    def estimar_risco(self) -> float:
        """Estima o risco total desta ameaça"""
        return (self.potencial_dano * 0.6 + 
                self.velocidade_propagacao * 0.3 +
                len(self.penetracao) * 0.1)


@dataclass
class AnticorpoNeural:
    """Uma defesa contra uma ameaça (anticorpo = resposta imune)"""
    
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    antigenio_id: str = ""                 # ID do antígeno que combate
    
    # Caracterização
    tipo_resposta: str = ""                # Tipo de resposta imune
    timestamp_criacao: datetime = field(default_factory=datetime.now)
    
    # Eficácia
    afinidade: float = 0.5                # 0-1: quão bem se liga ao antígeno
    potencia: float = 0.5                 # 0-1: força da neutralização
    especificidade: float = 0.9           # 0-1: específico vs. genérico
    
    # Ação
    mecanismo: str = ""                   # Como funciona
    tempo_acao_ms: int = 100              # Tempo para neutralizar
    recursos_necessarios: Dict[str, float] = field(default_factory=dict)
    
    # Status
    ativo: bool = True
    aplicacoes: int = 0                   # Quantas vezes foi usado
    taxa_sucesso: float = 0.0             # % de sucessos


@dataclass
class ThreatProfile:
    """Perfil de ameaça (conhece o "inimigo")"""
    
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    tipo_ameaca: TipoAmeaca
    
    # Conhecimento
    assinatura: str = ""                  # Padrão característico
    vetor_ataque: str = ""                # Como ataca
    metodo_propagacao: str = ""           # Como se espalha
    
    # Defesa
    anticorpos_conhecidos: List[str] = field(default_factory=list)  # IDs de anticorpos efetivos
    bloqueadores: List[str] = field(default_factory=list)  # Núcleos a bloquear
    
    # Histórico
    vezes_encontrada: int = 0
    vezes_neutralizada: int = 0
    taxa_sucesso_historica: float = 0.0
    
    timestamp_primeira_vista: datetime = field(default_factory=datetime.now)
    timestamp_ultima_vista: datetime = field(default_factory=datetime.now)

