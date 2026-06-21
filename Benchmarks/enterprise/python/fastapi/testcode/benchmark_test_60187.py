# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest60187(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = coalesce_blank(graphql_var)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
