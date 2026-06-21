# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse
import json


async def BenchmarkTest65694(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', graphql_var):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = graphql_var
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'Content-Language': str(processed)})
