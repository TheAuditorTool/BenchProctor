# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import ast


async def BenchmarkTest78320(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
