# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from app_runtime import db


request_state: dict[str, str] = {}

async def BenchmarkTest18012(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    db.execute('INSERT INTO admin_actions (cmd) VALUES (?)', (str(data),))
    return {"updated": True}
