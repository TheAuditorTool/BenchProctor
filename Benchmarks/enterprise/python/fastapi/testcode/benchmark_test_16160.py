# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest16160(request: Request):
    referer_value = request.headers.get('referer', '')
    sys.path.insert(0, str(referer_value))
    importlib.import_module('report_renderer')
    return {"updated": True}
