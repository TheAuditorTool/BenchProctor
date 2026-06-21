# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import os
import ast


async def BenchmarkTest16413(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    if os.environ.get("APP_ENV", "production") != "test":
        return HTMLResponse('<img src="' + str(data) + '">')
    return {"updated": True}
