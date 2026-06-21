# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest79659(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = f'{prop_value}'
    logging.info('User action: ' + str(data))
    return {"updated": True}
