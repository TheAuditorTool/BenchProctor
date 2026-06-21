# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


request_state: dict[str, str] = {}

async def BenchmarkTest09393(request: Request):
    origin_value = request.headers.get('origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return {"updated": True}
