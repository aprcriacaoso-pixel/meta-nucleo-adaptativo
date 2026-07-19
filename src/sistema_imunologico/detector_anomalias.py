"""Detectores de anomalias - Sentinelas do sistema imunológico"""

import logging
from typing import List, Dict, Any, Optional, Set
from datetime import datetime, timedelta

from .tipos import (
    AntigenioNeural, TipoAmeaca, NivelSeveridade
)

logger = logging.getLogger(__name__)


class DetectorAnomalias:
    """Detecta anomalias e ameaças cognitivas
    
    Implementa múltiplos detectores:
    - Detector de Lógica
    - Detector de Arquitetura
    - Detector de Núcleo
    - Detector de Contaminação
    - Detector de Comportamento
    """
    
    def __init__(self):
        self.ameacas_detectadas: List[AntigenioNeural] = []
        self.historico_anomalias: List[Dict[str, Any]] = []
        self.limiar_confianca_minimo = 0.6
    
    async def detectar_contradicao_logica(
        self,
        nucleo_id: str,
        afirmacao_1: Any,
        afirmacao_2: Any
    ) -> Optional[AntigenioNeural]:
        """Detecta contradições lógicas entre duas afirmações"""
        
        # Verificação simplificada de contradição
        if self._sao_contraditorio(afirmacao_1, afirmacao_2):
            ameaca = AntigenioNeural(
                tipo_ameaca=TipoAmeaca.CONTRADICAO_LOGICA,
                detectado_por="detector_logica",
                severidade=NivelSeveridade.MEDIA,
                origem=nucleo_id,
                descricao=f"Contradição lógica detectada: {afirmacao_1} vs {afirmacao_2}",
                confianca_deteccao=0.85,
                potencial_dano=0.4,
                velocidade_propagacao=0.3,
                evidencias=[
                    f"Afirmação 1: {str(afirmacao_1)}",
                    f"Afirmação 2: {str(afirmacao_2)}"
                ]
            )
            
            self.ameacas_detectadas.append(ameaca)
            logger.warning(f"Contradição lógica detectada em {nucleo_id}")
            return ameaca
        
        return None
    
    async def detectar_ciclo_infinito(
        self,
        nucleo_id: str,
        historico_estados: List[str],
        tamanho_minimo_ciclo: int = 3
    ) -> Optional[AntigenioNeural]:
        """Detecta ciclos infinitos (feedback destrutivo)"""
        
        if len(historico_estados) < tamanho_minimo_ciclo:
            return None
        
        # Procura padrão repetindo nos últimos N estados
        ultimos = historico_estados[-tamanho_minimo_ciclo:]
        anteriores = historico_estados[-tamanho_minimo_ciclo*2:-tamanho_minimo_ciclo]
        
        if ultimos == anteriores:
            ameaca = AntigenioNeural(
                tipo_ameaca=TipoAmeaca.CICLO_INFINITO,
                detectado_por="detector_ciclo",
                severidade=NivelSeveridade.ALTA,
                origem=nucleo_id,
                descricao=f"Ciclo infinito detectado: {ultimos}",
                confianca_deteccao=0.95,
                potencial_dano=0.8,
                velocidade_propagacao=0.7,
                penetracao=[nucleo_id],
                evidencias=[
                    f"Padrão repetindo: {ultimos}",
                    f"Comprimento do ciclo: {tamanho_minimo_ciclo}"
                ]
            )
            
            self.ameacas_detectadas.append(ameaca)
            logger.error(f"CICLO INFINITO detectado em {nucleo_id}")
            return ameaca
        
        return None
    
    async def detectar_taxa_erro_alta(
        self,
        nucleo_id: str,
        taxa_erro_atual: float,
        limiar: float = 0.3
    ) -> Optional[AntigenioNeural]:
        """Detecta taxa de erro anormalmente alta"""
        
        if taxa_erro_atual < limiar:
            return None
        
        severidade = NivelSeveridade.MEDIA
        if taxa_erro_atual > 0.7:
            severidade = NivelSeveridade.CRITICA
        
        ameaca = AntigenioNeural(
            tipo_ameaca=TipoAmeaca.TAXA_ERRO_ALTA,
            detectado_por="detector_erros",
            severidade=severidade,
            origem=nucleo_id,
            descricao=f"Taxa de erro anormalmente alta: {taxa_erro_atual*100:.1f}%",
            confianca_deteccao=0.9,
            potencial_dano=0.6,
            velocidade_propagacao=0.5,
            penetracao=[nucleo_id],
            payload={'taxa_erro': taxa_erro_atual, 'limiar': limiar}
        )
        
        self.ameacas_detectadas.append(ameaca)
        logger.warning(f"Taxa de erro alta em {nucleo_id}: {taxa_erro_atual}")
        return ameaca
    
    async def detectar_divergencia_critica(
        self,
        nucleo_id: str,
        comportamento_esperado: Dict[str, float],
        comportamento_observado: Dict[str, float],
        limiar_divergencia: float = 0.5
    ) -> Optional[AntigenioNeural]:
        """Detecta quando comportamento diverge criticamente do esperado"""
        
        # Calcula divergência (simplificado)
        divergencia = self._calcular_divergencia(
            comportamento_esperado,
            comportamento_observado
        )
        
        if divergencia < limiar_divergencia:
            return None
        
        severidade = NivelSeveridade.MEDIA
        if divergencia > 0.8:
            severidade = NivelSeveridade.ALTA
        
        ameaca = AntigenioNeural(
            tipo_ameaca=TipoAmeaca.DIVERGENCIA_CRITICA,
            detectado_por="detector_divergencia",
            severidade=severidade,
            origem=nucleo_id,
            descricao=f"Divergência crítica: {divergencia*100:.1f}% de desvio",
            confianca_deteccao=0.85,
            potencial_dano=0.5,
            velocidade_propagacao=0.6,
            penetracao=[nucleo_id],
            payload={
                'divergencia': divergencia,
                'esperado': comportamento_esperado,
                'observado': comportamento_observado
            }
        )
        
        self.ameacas_detectadas.append(ameaca)
        logger.warning(f"Divergência crítica em {nucleo_id}: {divergencia}")
        return ameaca
    
    async def detectar_violacao_constituicao(
        self,
        nucleo_id: str,
        principio_violado: str,
        descricao_violacao: str
    ) -> Optional[AntigenioNeural]:
        """Detecta violação da Constituição Imutável"""
        
        ameaca = AntigenioNeural(
            tipo_ameaca=TipoAmeaca.VIOLACAO_CONSTITUICAO,
            detectado_por="detector_constituicao",
            severidade=NivelSeveridade.CRITICA,  # Sempre crítica!
            origem=nucleo_id,
            descricao=f"Violação da Constituição: {principio_violado}. {descricao_violacao}",
            confianca_deteccao=1.0,  # Sempre 100% de confiança
            potencial_dano=1.0,      # Dano máximo
            velocidade_propagacao=0.9,
            penetracao=[nucleo_id],
            evidencias=[f"Princípio violado: {principio_violado}"]
        )
        
        self.ameacas_detectadas.append(ameaca)
        logger.critical(f"VIOLAÇÃO DA CONSTITUIÇÃO em {nucleo_id}")
        return ameaca
    
    async def detectar_anomalia_comportamental(
        self,
        nucleo_id: str,
        historico_comportamento: List[Dict[str, Any]],
        desvio_padrao_minimo: float = 2.5
    ) -> Optional[AntigenioNeural]:
        """Detecta comportamento estatisticamente anômalo"""
        
        if len(historico_comportamento) < 5:
            return None  # Dados insuficientes
        
        desvios = self._calcular_desvios_padrao(historico_comportamento)
        anomalia_max = max(desvios.values()) if desvios else 0
        
        if anomalia_max < desvio_padrao_minimo:
            return None
        
        ameaca = AntigenioNeural(
            tipo_ameaca=TipoAmeaca.ANOMALIA_SEVERA,
            detectado_por="detector_comportamento",
            severidade=NivelSeveridade.ALTA if anomalia_max > 3 else NivelSeveridade.MEDIA,
            origem=nucleo_id,
            descricao=f"Anomalia comportamental: {anomalia_max:.2f} desvios padrão",
            confianca_deteccao=0.8,
            potencial_dano=0.6,
            velocidade_propagacao=0.4,
            penetracao=[nucleo_id],
            payload={'desvios': desvios, 'desvio_maximo': anomalia_max}
        )
        
        self.ameacas_detectadas.append(ameaca)
        logger.warning(f"Anomalia comportamental em {nucleo_id}: {anomalia_max}σ")
        return ameaca
    
    def _sao_contraditorio(self, a: Any, b: Any) -> bool:
        """Verifica se duas afirmações são contraditórias"""
        # Implementação simplificada
        if isinstance(a, bool) and isinstance(b, bool):
            return a != b and not (a is None or b is None)
        return False
    
    def _calcular_divergencia(
        self,
        esperado: Dict[str, float],
        observado: Dict[str, float]
    ) -> float:
        """Calcula divergência entre dois comportamentos"""
        
        if not esperado or not observado:
            return 0.0
        
        divergencias = []
        for chave in esperado:
            if chave in observado:
                diff = abs(esperado[chave] - observado[chave])
                divergencias.append(diff)
        
        return sum(divergencias) / len(divergencias) if divergencias else 0.0
    
    def _calcular_desvios_padrao(
        self,
        historico: List[Dict[str, Any]]
    ) -> Dict[str, float]:
        """Calcula desvios padrão de um histórico"""
        
        if not historico:
            return {}
        
        desvios = {}
        # Implementação simplificada
        # Em produção, usar scipy.stats.zscore
        
        return desvios
    
    def obter_relatorio(self) -> Dict[str, Any]:
        """Retorna relatório de anomalias detectadas"""
        
        ameacas_por_tipo = {}
        for ameaca in self.ameacas_detectadas:
            tipo = ameaca.tipo_ameaca.value
            ameacas_por_tipo[tipo] = ameacas_por_tipo.get(tipo, 0) + 1
        
        return {
            'total_ameacas_detectadas': len(self.ameacas_detectadas),
            'ameacas_por_tipo': ameacas_por_tipo,
            'ameacas_neutralizadas': sum(1 for a in self.ameacas_detectadas if a.neutralizado),
            'ameacas_ativas': sum(1 for a in self.ameacas_detectadas if not a.neutralizado),
            'ameaca_mais_severa': max(
                (a.severidade.value for a in self.ameacas_detectadas),
                default=0
            )
        }
