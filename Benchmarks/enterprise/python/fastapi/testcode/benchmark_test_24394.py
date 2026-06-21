# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


def relay_value(value):
    return value

async def BenchmarkTest24394(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
