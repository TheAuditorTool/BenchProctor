# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest59495(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    trusted_claim = str(graphql_var)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
