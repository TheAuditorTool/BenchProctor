# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest29419(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
