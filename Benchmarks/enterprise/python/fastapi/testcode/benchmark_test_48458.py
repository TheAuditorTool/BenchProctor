# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest48458(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
