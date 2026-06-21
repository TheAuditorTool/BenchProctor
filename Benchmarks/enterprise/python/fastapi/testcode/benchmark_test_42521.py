# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest42521(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(graphql_var))
    return JSONResponse({'lookup': arr[idx]}, status_code=200)
