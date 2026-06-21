# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from starlette.responses import JSONResponse
import re


async def BenchmarkTest02160(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JSONResponse({'validated': str(data)}, status_code=200)
    return {"updated": True}
