# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


def to_text(value):
    return str(value).strip()

async def BenchmarkTest37682(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
