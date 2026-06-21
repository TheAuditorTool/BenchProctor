# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest27550(request: Request):
    ua_value = request.headers.get('user-agent', '')
    sys.path.insert(0, str(ua_value))
    importlib.import_module('report_renderer')
    return {"updated": True}
