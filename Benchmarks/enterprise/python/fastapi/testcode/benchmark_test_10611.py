# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
from app_runtime import db


async def BenchmarkTest10611(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return {"updated": True}
