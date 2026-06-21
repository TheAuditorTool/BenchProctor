# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from starlette.responses import JSONResponse
import json
import hashlib
from app_runtime import db


def normalise_input(value):
    return value.strip()

async def BenchmarkTest81486(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return JSONResponse({'error': 'integrity check failed'}, status_code=502)
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return {"updated": True}
