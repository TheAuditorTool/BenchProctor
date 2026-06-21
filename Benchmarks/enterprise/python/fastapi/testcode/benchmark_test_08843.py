# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
from app_runtime import db


async def BenchmarkTest08843(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(env_value),))
    logging.info('request processed')
    return {"updated": True}
