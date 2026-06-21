# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time
import ast


async def BenchmarkTest64768(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
