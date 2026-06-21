# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest04504(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
