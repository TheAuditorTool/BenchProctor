# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json
import re


async def BenchmarkTest06531(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    if re.search('[a-zA-Z0-9_-]+', str(graphql_var)):
        return JSONResponse({'validated': str(graphql_var)}, status_code=200)
    return {"updated": True}
