# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ast


async def BenchmarkTest17524(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    raise RuntimeError('processing failed: ' + str(data))
    return {"updated": True}
