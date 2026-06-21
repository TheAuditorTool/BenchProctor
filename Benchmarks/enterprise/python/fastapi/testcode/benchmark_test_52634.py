# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast


async def BenchmarkTest52634(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return {"updated": True}
