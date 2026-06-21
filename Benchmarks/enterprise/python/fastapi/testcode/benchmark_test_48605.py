# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest48605(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
