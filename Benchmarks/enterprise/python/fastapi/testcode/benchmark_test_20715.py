# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest20715(request: Request):
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    request_state['last_input'] = db_value
    data = request_state['last_input']
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
