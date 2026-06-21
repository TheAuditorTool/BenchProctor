# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest27752(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = (lambda v: v.strip())(ua_value)
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
