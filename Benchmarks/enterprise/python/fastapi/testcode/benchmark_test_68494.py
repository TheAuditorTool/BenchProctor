# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import subprocess
import ast


async def BenchmarkTest68494(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
