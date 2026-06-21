# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest19508(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    eval(compile("with open('/var/app/data/' + str(data), 'w') as fh:\n    fh.write('data')", '<sink>', 'exec'))
    return {"updated": True}
