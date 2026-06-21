# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import ast


async def BenchmarkTest59096(request: Request):
    referer_value = request.headers.get('referer', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    def _primary():
        os.system('echo ' + str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
