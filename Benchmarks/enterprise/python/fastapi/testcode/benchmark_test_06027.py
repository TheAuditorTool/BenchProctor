# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest06027(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
