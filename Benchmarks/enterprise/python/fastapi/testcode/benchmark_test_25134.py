# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest25134(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
