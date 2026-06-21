# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from dataclasses import dataclass
from starlette.responses import JSONResponse
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest79395(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(processed)})
