import gzip
import sh as pbs
from sh import pg_dump


AUN NO FUNCIONA

with gzip.open('respaldo_base_gestion_rrhh.gz', 'wb') as f:
  pg_dump('-h', 'localhost', '-U', 'admin', 'Gestion_RRHH', _out=f)
