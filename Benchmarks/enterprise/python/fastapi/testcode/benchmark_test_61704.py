# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


request_state: dict[str, str] = {}

async def BenchmarkTest61704(request: Request):
    path_value = request.path_params.get('id', '')
    request_state['last_input'] = path_value
    data = request_state['last_input']
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return {"updated": True}
