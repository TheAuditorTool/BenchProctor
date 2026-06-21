# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
import ast


async def BenchmarkTest27975(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    if time.time() > 1000000000:
        os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
