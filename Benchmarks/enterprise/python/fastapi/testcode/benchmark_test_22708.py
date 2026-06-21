# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
from app_runtime import db


async def BenchmarkTest22708(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(cookie_value),))
    logging.info('audit actor=%s action=revoke_sessions', str(cookie_value))
    return {"updated": True}
