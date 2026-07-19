"""Fábrica de Anticorpos - Cria defesas contra ameaças"""

import logging
from typing import Optional, Dict, Any
from datetime import datetime

from .tipos import (
    AnticorpoNeural, AntigenioNeural, TipoAmeaca
)

logger = logging.getLogger(__name__)


class AnticorpoFactory:
    """Manufatura anticorpos (defesas) contra antígenos (ameaças)"""
    
    def __init__(self):
        self.anticorpos_criados: Dict[str, AnticorpoNeural] = {}
        self.blueprints_respostas = self._carregar_blueprints()
    
    def _carregar_blueprints(self) -> Dict[TipoAmeaca, Dict[str, Any]]:
        """Carrega blueprints de respostas para cada tipo de ameaça"""
        
        return {
            TipoAmeaca.CONTRADICAO_LOGICA: {
                'tipo_resposta': 'validacao_logica',
                'mecanismo': 'Força revisão de premissas',
                'tempo_acao_ms': 50,
                'afinidade': 0.9,
                'potencia': 0.7
            },
            TipoAmeaca.CICLO_INFINITO: {
                'tipo_resposta': 'quebra_ciclo',
                'mecanismo': 'Interrompe núcleo e reinicia estado',
                'tempo_acao_ms': 10,
                'afinidade': 0.95,
                'potencia': 0.95
            },
            TipoAmeaca.TAXA_ERRO_ALTA: {
                'tipo_resposta': 'isolamento_nucleoarqreset',
                'mecanismo': 'Isola núcleo e reseta pesos',
                'tempo_acao_ms': 100,
                'afinidade': 0.85,
                'potencia': 0.8
            },
            TipoAmeaca.DIVERGENCIA_CRITICA: {
                'tipo_resposta': 'recalibracao',
                'mecanismo': 'Recalibra pesos para comportamento esperado',
                'tempo_acao_ms': 200,
                'afinidade': 0.75,
                'potencia': 0.7
            },
            TipoAmeaca.VIOLACAO_CONSTITUICAO: {
                'tipo_resposta': 'bloqueio_total',
                'mecanismo': 'Bloqueia núcleo completamente',
                'tempo_acao_ms': 5,
                'afinidade': 1.0,
                'potencia': 1.0
            },
            TipoAmeaca.ANOMALIA_SEVERA: {
                'tipo_resposta': 'quarentena_investigacao',
                'mecanismo': 'Quarentena e análise profunda',
                'tempo_acao_ms': 500,
                'afinidade': 0.8,
                'potencia': 0.6
            },
        }
    
    async def criar_anticorpo(self, antigenio: AntigenioNeural) -> AnticorpoNeural:
        """Cria um anticorpo (defesa) para um antígeno (ameaça)"""
        
        # Procura blueprint para este tipo de ameaça
        blueprint = self.blueprints_respostas.get(
            antigenio.tipo_ameaca,
            self._blueprint_generico()
        )
        
        # Monta anticorpo
        anticorpo = AnticorpoNeural(
            antigenio_id=antigenio.id,
            tipo_resposta=blueprint['tipo_resposta'],
            mecanismo=blueprint['mecanismo'],
            tempo_acao_ms=blueprint['tempo_acao_ms'],
            afinidade=blueprint.get('afinidade', 0.7),
            potencia=blueprint.get('potencia', 0.6),
            especificidade=self._calcular_especificidade(antigenio)
        )
        
        # Registra
        self.anticorpos_criados[anticorpo.id] = anticorpo
        
        logger.info(f"Anticorpo criado para ameaça {antigenio.tipo_ameaca.value}: "
                   f"{anticorpo.tipo_resposta}")
        
        return anticorpo
    
    def _blueprint_generico(self) -> Dict[str, Any]:
        """Blueprint genérico para ameaças desconhecidas"""
        return {
            'tipo_resposta': 'monitoramento_ativo',
            'mecanismo': 'Monitora de perto para ameaças adicionais',
            'tempo_acao_ms': 1000,
            'afinidade': 0.5,
            'potencia': 0.4
        }
    
    def _calcular_especificidade(self, antigenio: AntigenioNeural) -> float:
        """Calcula a especificidade do anticorpo
        
        Mais específico = melhor funciona contra este antígeno exato
        Menos específico = funciona contra classe de antígenos similar
        """
        
        if antigenio.confianca_deteccao > 0.9:
            return 0.95  # Muito específico
        elif antigenio.confianca_deteccao > 0.7:
            return 0.8   # Específico
        else:
            return 0.6   # Genérico
    
    def obter_anticorpo_para(self, antigenio_id: str) -> Optional[AnticorpoNeural]:
        """Busca anticorpo efetivo para um antígeno"""
        
        for anticorpo in self.anticorpos_criados.values():
            if anticorpo.antigenio_id == antigenio_id and anticorpo.ativo:
                return anticorpo
        
        return None
    
    def obter_anticorpos_ativos(self) -> int:
        """Retorna número de anticorpos ativos"""
        return sum(1 for a in self.anticorpos_criados.values() if a.ativo)
