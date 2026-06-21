# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest02567(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    kind = 'json' if str(config_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = config_value
            data = parsed
        case _:
            data = config_value
    logging.info('User action: ' + str(data))
    return {"updated": True}
