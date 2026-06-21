# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest62445(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    return HTMLResponse(str(processed))
