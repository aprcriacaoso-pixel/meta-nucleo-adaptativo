"""Sistema Imunológico do MNA

Mecanismo de defesa cognitiva que:
- Detecta ideias ruins, arquiteturas frágeis
- Identifica núcleos defeituosos
- Quarentena e neutraliza ameaças
- Limpa contaminação antes que se espalhe
"""

from .tipos import (
    TipoAmeaca, AmeacaCognitiva, EstadoImune,
    AntigenioNeural, AnticorpoNeural
)
from .detector_anomalias import DetectorAnomalias
from .antigenio_processor import AntigenioProcessor
from .anticorpo_factory import AnticorpoFactory
from .quarentena import SistemaQuarentena
from .guardiao_imune import Guardiao

__all__ = [
    'TipoAmeaca',
    'AmeacaCognitiva',
    'EstadoImune',
    'AntigenioNeural',
    'AnticorpoNeural',
    'DetectorAnomalias',
    'AntigenioProcessor',
    'AnticorpoFactory',
    'SistemaQuarentena',
    'Guardiao',
]
