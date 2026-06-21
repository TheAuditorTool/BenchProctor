# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import base64
import importlib
import sys


async def BenchmarkTest70904(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
