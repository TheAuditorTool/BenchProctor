# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


async def BenchmarkTest71956(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('SELECT * FROM "' + str(env_value).replace('"', '""') + '"')
    return {"updated": True}
