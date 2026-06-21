# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from app_runtime import db


async def BenchmarkTest59339(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    _resp = requests.get(str(data))
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
