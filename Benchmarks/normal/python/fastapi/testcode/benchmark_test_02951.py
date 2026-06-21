# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
import time
import ast


async def BenchmarkTest02951(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    if time.time() > 1000000000:
        return RedirectResponse(url=str(data))
    return {"updated": True}
