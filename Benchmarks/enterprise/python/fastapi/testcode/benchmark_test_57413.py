# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import base64
from app_runtime import db


async def BenchmarkTest57413(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
