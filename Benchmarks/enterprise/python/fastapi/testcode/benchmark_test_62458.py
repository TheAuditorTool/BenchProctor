# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


request_state: dict[str, str] = {}

async def BenchmarkTest62458(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return {"updated": True}
