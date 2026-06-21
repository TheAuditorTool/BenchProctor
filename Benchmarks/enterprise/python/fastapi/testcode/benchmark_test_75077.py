# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest75077(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
