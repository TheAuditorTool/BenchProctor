# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import ast


async def BenchmarkTest65265(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
