# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest62053(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
