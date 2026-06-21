# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest02035(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = ua_value if ua_value else 'default'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
