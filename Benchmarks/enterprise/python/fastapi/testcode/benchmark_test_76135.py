# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest76135(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
