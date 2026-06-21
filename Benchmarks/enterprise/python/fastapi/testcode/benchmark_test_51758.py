# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
from app_runtime import db


async def BenchmarkTest51758(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(env_value),))
    logging.info('audit actor=%s action=revoke_sessions', str(env_value))
    return {"updated": True}
