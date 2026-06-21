# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging


request_state: dict[str, str] = {}

async def BenchmarkTest02220(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return {"updated": True}
