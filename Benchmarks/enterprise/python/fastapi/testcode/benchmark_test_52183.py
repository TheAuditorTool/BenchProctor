# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import logging
import os
from app_runtime import db


async def BenchmarkTest52183(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return {"updated": True}
