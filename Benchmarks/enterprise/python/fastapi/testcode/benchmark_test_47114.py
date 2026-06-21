# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess
import ast


async def BenchmarkTest47114(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
