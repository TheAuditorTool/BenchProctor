# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest10559(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    db.execute('UPDATE users SET role = ? WHERE name = ?', ('admin', str(data)))
    return {"updated": True}
