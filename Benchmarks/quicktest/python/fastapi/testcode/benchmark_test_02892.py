# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import ast


async def BenchmarkTest02892(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
