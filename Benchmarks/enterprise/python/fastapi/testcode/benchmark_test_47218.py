# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time
import ast


async def BenchmarkTest47218(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
