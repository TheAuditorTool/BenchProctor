# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest34585(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = ' '.join(str(prop_value).split())
    logging.info('User action: ' + str(data))
    return {"updated": True}
