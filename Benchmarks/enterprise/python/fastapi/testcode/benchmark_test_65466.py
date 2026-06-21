# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest65466(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    processed = data[:64]
    if str(processed) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
