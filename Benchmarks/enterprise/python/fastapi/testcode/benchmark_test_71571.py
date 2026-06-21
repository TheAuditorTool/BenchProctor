# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import time
import ast
import subprocess


async def BenchmarkTest71571(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
