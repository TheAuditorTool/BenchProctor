# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import ast


async def BenchmarkTest34697(request: Request):
    ua_value = request.headers.get('user-agent', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
