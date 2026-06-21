# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest21678(request: Request):
    origin_value = request.headers.get('origin', '')
    data = origin_value if origin_value else 'default'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
