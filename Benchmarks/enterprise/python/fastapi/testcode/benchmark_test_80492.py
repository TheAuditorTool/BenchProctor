# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


request_state: dict[str, str] = {}

async def BenchmarkTest80492(request: Request):
    query_array = request.query_params.get('items', '')
    request_state['last_input'] = query_array
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return {"updated": True}
