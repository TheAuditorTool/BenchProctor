# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest62330(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
