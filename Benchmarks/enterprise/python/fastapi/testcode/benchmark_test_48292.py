# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest48292(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return {"updated": True}
