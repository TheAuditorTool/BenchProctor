# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest21838(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    parts = []
    for token in str(prop_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return {"updated": True}
