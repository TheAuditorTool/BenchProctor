# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest37926(request: Request):
    origin_value = request.headers.get('origin', '')
    sys.path.insert(0, str(origin_value))
    importlib.import_module('report_renderer')
    return {"updated": True}
