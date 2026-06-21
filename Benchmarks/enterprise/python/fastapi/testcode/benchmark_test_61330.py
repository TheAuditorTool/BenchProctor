# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest61330(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(env_value),))
    return {"updated": True}
