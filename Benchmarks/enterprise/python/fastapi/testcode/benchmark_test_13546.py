# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


async def BenchmarkTest13546(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return {"updated": True}
