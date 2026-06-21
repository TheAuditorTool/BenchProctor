# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
import sys


async def BenchmarkTest25149(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
