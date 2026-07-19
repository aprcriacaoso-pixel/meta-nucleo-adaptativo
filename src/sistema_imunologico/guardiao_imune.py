"""Guardião do Sistema Imunológico - Orquestração da resposta imune"""

import asyncio
import logging
from typing import List, Dict, Optional, Any
from datetime import datetime

from .tipos import (
    AntigenioNeural, AnticorpoNeural, EstadoImune,
    TipoAmeaca, NivelSeveridade
)
from .detector_anomalias import DetectorAnomalias
from .anticorpo_factory import AnticorpoFactory
from .quarentena import SistemaQuarentena, NivelQuarentena

logger = logging.getLogger(__name__)


class Guardiao:
    """O Guardião - Coordena a resposta imunológica completa
    
    Responsabilidades:
    - Escuta os detectores
    - Fabrica anticorpos
    - Ativa quarentena
    - Orquestra limpeza
    - Mantém vigilância
    """
    
    def __init__(self):
        self.detector = DetectorAnomalias()
        self.fabrica_anticorpos = AnticorpoFactory()
        self.quarentena = SistemaQuarentena()
        
        # Estado
        self.estado_imune = EstadoImune.VIGILANCIA
        self.ameacas_ativas: List[AntigenioNeural] = []
        self.anticorpos_implantados: Dict[str, AnticorpoNeural] = {}
        
        # Métricas
        self.timestamp_ativacao = datetime.now()
        self.total_ameacas_neutralizadas = 0
        self.total_intervencoes = 0
    
    async def processar_ameaca(
        self,
        ameaca: AntigenioNeural
    ) -> Dict[str, Any]:
        """Processa uma ameaça detectada (pipeline imunológico)
        
        1. Confirma ameaça
        2. Classifica severidade
        3. Fabrica anticorpo
        4. Implanta defesa
        5. Quarentena se necessário
        """
        
        logger.info(f"Guardião iniciando processamento de ameaça: "
                   f"{ameaca.tipo_ameaca.value}")
        
        # Atualiza estado
        self.estado_imune = EstadoImune.ALERTA
        self.ameacas_ativas.append(ameaca)
        
        # Resposta baseada em severidade
        if ameaca.severidade == NivelSeveridade.CATASTROFICA:
            return await self._resposta_catastrofica(ameaca)
        elif ameaca.severidade == NivelSeveridade.CRITICA:
            return await self._resposta_critica(ameaca)
        elif ameaca.severidade == NivelSeveridade.ALTA:
            return await self._resposta_agressiva(ameaca)
        elif ameaca.severidade == NivelSeveridade.MEDIA:
            return await self._resposta_moderada(ameaca)
        else:
            return await self._resposta_leve(ameaca)
    
    async def _resposta_leve(self, ameaca: AntigenioNeural) -> Dict[str, Any]:
        """Resposta para ameaças leves"""
        
        logger.debug(f"Resposta LEVE para {ameaca.tipo_ameaca.value}")
        
        # Apenas monitora
        return {
            'acao': 'monitoramento',
            'severidade': 'baixa',
            'nucleos_afetados': ameaca.penetracao,
            'anticorpos_implantados': 0
        }
    
    async def _resposta_moderada(self, ameaca: AntigenioNeural) -> Dict[str, Any]:
        """Resposta para ameaças moderadas"""
        
        logger.info(f"Resposta MODERADA para {ameaca.tipo_ameaca.value}")
        
        # Cria anticorpo
        anticorpo = await self.fabrica_anticorpos.criar_anticorpo(ameaca)
        self.anticorpos_implantados[anticorpo.id] = anticorpo
        
        # Monitora de perto
        return {
            'acao': 'anticorpo_implantado',
            'severidade': 'média',
            'anticorpo_id': anticorpo.id,
            'tipo_resposta': anticorpo.tipo_resposta
        }
    
    async def _resposta_agressiva(self, ameaca: AntigenioNeural) -> Dict[str, Any]:
        """Resposta para ameaças altas"""
        
        logger.warning(f"Resposta AGRESSIVA para {ameaca.tipo_ameaca.value}")
        
        self.estado_imune = EstadoImune.DEFESA_ATIVA
        self.total_intervencoes += 1
        
        # Cria anticorpo
        anticorpo = await self.fabrica_anticorpos.criar_anticorpo(ameaca)
        self.anticorpos_implantados[anticorpo.id] = anticorpo
        
        # Quarentena o núcleo afetado
        for nucleo_id in ameaca.penetracao:
            await self.quarentena.quarentena_nucleo(
                nucleo_id,
                ameaca,
                NivelQuarentena.MODERADA
            )
        
        return {
            'acao': 'quarentena_e_anticorpo',
            'severidade': 'alta',
            'anticorpo_id': anticorpo.id,
            'nucleos_quarentenados': ameaca.penetracao
        }
    
    async def _resposta_critica(self, ameaca: AntigenioNeural) -> Dict[str, Any]:
        """Resposta para ameaças críticas"""
        
        logger.error(f"Resposta CRÍTICA para {ameaca.tipo_ameaca.value}")
        
        self.estado_imune = EstadoImune.QUARENTENA
        self.total_intervencoes += 1
        
        # Quarentena severa
        for nucleo_id in ameaca.penetracao:
            await self.quarentena.quarentena_nucleo(
                nucleo_id,
                ameaca,
                NivelQuarentena.SEVERA
            )
        
        # Cria anticorpo agressivo
        anticorpo = await self.fabrica_anticorpos.criar_anticorpo(ameaca)
        self.anticorpos_implantados[anticorpo.id] = anticorpo
        
        return {
            'acao': 'quarentena_severa',
            'severidade': 'crítica',
            'nucleos_desativados': ameaca.penetracao,
            'anticorpo_id': anticorpo.id
        }
    
    async def _resposta_catastrofica(self, ameaca: AntigenioNeural) -> Dict[str, Any]:
        """Resposta para ameaças catastróficas - SHUTDOWN DE EMERGÊNCIA"""
        
        logger.critical(f"RESPOSTA CATASTRÓFICA ACIONADA: {ameaca.tipo_ameaca.value}")
        
        self.estado_imune = EstadoImune.CRITICA
        self.total_intervencoes += 1
        
        # Tenta desativar TODO o sistema se necessário
        # Em produção, isso dispararia alarmes máximos
        
        return {
            'acao': 'emergency_shutdown',
            'severidade': 'catastrófica',
            'mensagem': 'SISTEMA IMUNOLÓGICO ACIONOU SHUTDOWN DE EMERGÊNCIA',
            'motivo': ameaca.descricao
        }
    
    async def executar_ciclo_vigilancia(self, intervalo_ms: float = 100.0) -> None:
        """Executa ciclo contínuo de vigilância"""
        
        while True:
            try:
                # Limpa ameaças neutralizadas
                ameacas_ativas = [
                    a for a in self.ameacas_ativas if not a.neutralizado
                ]
                self.ameacas_ativas = ameacas_ativas
                
                # Monitora quarentena
                alteracoes = await self.quarentena.monitorar_quarentena()
                
                # Se não há ameaças ativas, volta a vigilância
                if not self.ameacas_ativas and self.estado_imune != EstadoImune.VIGILANCIA:
                    self.estado_imune = EstadoImune.VIGILANCIA
                    logger.info("Sistema imunológico em vigilância normal")
                
                await asyncio.sleep(intervalo_ms / 1000.0)
                
            except Exception as e:
                logger.error(f"Erro em ciclo de vigilância: {e}")
    
    def obter_relatorio_imune(self) -> Dict[str, Any]:
        """Retorna relatório completo do sistema imunológico"""
        
        return {
            'timestamp': datetime.now().isoformat(),
            'estado': self.estado_imune.value,
            'ameacas_ativas': len(self.ameacas_ativas),
            'anticorpos_implantados': len(self.anticorpos_implantados),
            'total_intervencoes': self.total_intervencoes,
            'total_neutralizadas': self.total_ameacas_neutralizadas,
            'detalhes_detector': self.detector.obter_relatorio(),
            'detalhes_quarentena': self.quarentena.obter_status_quarentena(),
            'ameacas_ativas_lista': [
                {
                    'id': a.id,
                    'tipo': a.tipo_ameaca.value,
                    'severidade': a.severidade.name,
                    'origem': a.origem
                }
                for a in self.ameacas_ativas[:5]  # Top 5
            ]
        }
