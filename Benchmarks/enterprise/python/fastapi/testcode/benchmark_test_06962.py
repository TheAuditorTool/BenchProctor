# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from types import SimpleNamespace
from app_runtime import db


async def BenchmarkTest06962(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(data),))
    return {"updated": True}
