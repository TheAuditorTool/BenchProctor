# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import ast


async def BenchmarkTest17222(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    def _primary():
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return {"updated": True}
