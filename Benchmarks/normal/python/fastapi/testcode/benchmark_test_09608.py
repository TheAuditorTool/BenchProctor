# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import json
from app_runtime import db


async def BenchmarkTest09608(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
