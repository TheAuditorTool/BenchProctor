# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


request_state: dict[str, str] = {}

async def BenchmarkTest57059(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return {"updated": True}
