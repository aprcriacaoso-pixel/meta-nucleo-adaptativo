"""Sistema de Quarentena - Isolamento de ameaças"""

import logging
from typing import List, Dict, Optional, Set
from datetime import datetime, timedelta
from enum import Enum

from .tipos import AntigenioNeural, AnticorpoNeural

logger = logging.getLogger(__name__)


class NivelQuarentena(Enum):
    """Níveis de isolamento"""
    LEVE = 1           # Monitoramento, sem bloqueio
    MODERADA = 2       # Restrito: sem entrada/saída de sinais
    SEVERA = 3         # Completamente isolado
    DESATIVACAO = 4    # Núcleo desativado


class SistemaQuarentena:
    """Gerencia isolamento de núcleos infectados
    
    Funcionalidades:
    - Quarentena núcleos comprometidos
    - Bloqueia propagação de ameaças
    - Monitora durante isolamento
    - Reintegração controlada
    """
    
    def __init__(self):
        self.nucleos_em_quarentena: Dict[str, Dict] = {}
        self.bloqueios_sinapses: Set[str] = set()  # IDs de sinapses bloqueadas
        self.historico_quarentena: List[Dict] = []
    
    async def quarentena_nucleo(
        self,
        nucleo_id: str,
        antigenio: AntigenioNeural,
        nivel: NivelQuarentena = NivelQuarentena.MODERADA
    ) -> bool:
        """Coloca um núcleo em quarentena"""
        
        self.nucleos_em_quarentena[nucleo_id] = {
            'nucleo_id': nucleo_id,
            'antigenio_id': antigenio.id,
            'nivel': nivel,
            'timestamp_inicio': datetime.now(),
            'motivo': antigenio.descricao,
            'bloqueios_entrada': [],
            'bloqueios_saida': [],
            'sinais_interceptados': 0
        }
        
        logger.warning(f"Núcleo {nucleo_id} em quarentena ({nivel.name})")
        return True
    
    async def bloquear_sinapse(
        self,
        sinapse_id: str,
        origem: str,
        destino: str
    ) -> bool:
        """Bloqueia uma sinapse para evitar propagação"""
        
        self.bloqueios_sinapses.add(sinapse_id)
        
        logger.info(f"Sinapse bloqueada: {origem} -> {destino}")
        return True
    
    def pode_transmitir_sinal(
        self,
        origem_id: str,
        destino_id: str,
        sinapse_id: str
    ) -> bool:
        """Verifica se um sinal pode ser transmitido"""
        
        # Sinapse bloqueada?
        if sinapse_id in self.bloqueios_sinapses:
            return False
        
        # Origem em quarentena com bloqueio de saída?
        if origem_id in self.nucleos_em_quarentena:
            quarentena = self.nucleos_em_quarentena[origem_id]
            if quarentena['nivel'] in (NivelQuarentena.MODERADA, 
                                      NivelQuarentena.SEVERA,
                                      NivelQuarentena.DESATIVACAO):
                return False
        
        # Destino em quarentena com bloqueio de entrada?
        if destino_id in self.nucleos_em_quarentena:
            quarentena = self.nucleos_em_quarentena[destino_id]
            if quarentena['nivel'] in (NivelQuarentena.MODERADA, 
                                      NivelQuarentena.SEVERA,
                                      NivelQuarentena.DESATIVACAO):
                return False
        
        return True
    
    async def monitorar_quarentena(self) -> List[Dict]:
        """Monitora núcleos em quarentena
        
        Retorna alterações ou indicadores de contaminação
        """
        
        alteracoes = []
        nucleos_liberaveis = []
        
        for nucleo_id, info in self.nucleos_em_quarentena.items():
            tempo_em_quarentena = (
                datetime.now() - info['timestamp_inicio']
            ).total_seconds() / 60  # em minutos
            
            # Critério de liberação: sem sinais suspeitos por 5 minutos
            if tempo_em_quarentena > 5 and info['sinais_interceptados'] == 0:
                nucleos_liberaveis.append(nucleo_id)
                alteracoes.append({
                    'tipo': 'candidato_liberacao',
                    'nucleo_id': nucleo_id,
                    'tempo_quarentena_min': tempo_em_quarentena
                })
        
        return alteracoes
    
    async def liberar_quarentena(
        self,
        nucleo_id: str,
        remover_bloqueios: bool = False
    ) -> bool:
        """Remove núcleo de quarentena"""
        
        if nucleo_id not in self.nucleos_em_quarentena:
            return False
        
        info = self.nucleos_em_quarentena[nucleo_id]
        
        self.historico_quarentena.append({
            'nucleo_id': nucleo_id,
            'timestamp_inicio': info['timestamp_inicio'],
            'timestamp_fim': datetime.now(),
            'motivo': info['motivo'],
            'sinais_interceptados': info['sinais_interceptados']
        })
        
        del self.nucleos_em_quarentena[nucleo_id]
        
        # Remove bloqueios se solicitado
        if remover_bloqueios:
            # Isso seria feito gradualmente em produção
            pass
        
        logger.info(f"Núcleo {nucleo_id} liberado da quarentena")
        return True
    
    def obter_status_quarentena(self) -> Dict:
        """Retorna status do sistema de quarentena"""
        
        return {
            'nucleos_em_quarentena': len(self.nucleos_em_quarentena),
            'sinapses_bloqueadas': len(self.bloqueios_sinapses),
            'historico_liberacoes': len(self.historico_quarentena),
            'nucleos_quarentenados': list(self.nucleos_em_quarentena.keys())
        }
