# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest09486(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
