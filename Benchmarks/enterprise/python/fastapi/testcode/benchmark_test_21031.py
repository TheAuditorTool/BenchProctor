# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
from app_runtime import db


async def BenchmarkTest21031(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
