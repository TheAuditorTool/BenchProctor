# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import json


async def BenchmarkTest72559(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
