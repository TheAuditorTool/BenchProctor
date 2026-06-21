# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest72914(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(env_value),))
    return {"updated": True}
