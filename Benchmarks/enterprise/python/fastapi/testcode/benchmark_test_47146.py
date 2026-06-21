# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


def relay_value(value):
    return value

async def BenchmarkTest47146(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
