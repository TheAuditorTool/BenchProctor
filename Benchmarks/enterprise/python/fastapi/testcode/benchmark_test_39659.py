# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
import sys


async def BenchmarkTest39659(request: Request):
    auth_header = request.headers.get('authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
