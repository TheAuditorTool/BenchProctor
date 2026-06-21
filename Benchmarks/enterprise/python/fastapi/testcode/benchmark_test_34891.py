# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest34891(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    db.execute('DELETE FROM accounts WHERE id = ?', (str(graphql_var),))
    return {"updated": True}
