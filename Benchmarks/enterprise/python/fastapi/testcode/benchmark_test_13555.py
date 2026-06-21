# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


async def BenchmarkTest13555(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    pending = list(str(prop_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    logging.info('User action: ' + str(data))
    return {"updated": True}
