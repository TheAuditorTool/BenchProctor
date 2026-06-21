# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest11381(request: Request):
    host_value = request.headers.get('host', '')
    sys.path.insert(0, str(host_value))
    importlib.import_module('report_renderer')
    return {"updated": True}
