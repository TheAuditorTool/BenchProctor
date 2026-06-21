# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import time
import ast
import importlib
import sys


async def BenchmarkTest37608(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return {"updated": True}
