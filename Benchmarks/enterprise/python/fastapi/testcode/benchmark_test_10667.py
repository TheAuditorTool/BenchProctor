# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest10667(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    parts = str(prop_value).split(',')
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return {"updated": True}
