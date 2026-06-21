# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest53940(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
