# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest30813(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    request_state['last_input'] = forwarded_ip
    data = request_state['last_input']
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
