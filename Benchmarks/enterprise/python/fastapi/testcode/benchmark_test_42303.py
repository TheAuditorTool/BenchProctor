# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


request_state: dict[str, str] = {}

async def BenchmarkTest42303(request: Request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    request_state['last_input'] = prop_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return {"updated": True}
