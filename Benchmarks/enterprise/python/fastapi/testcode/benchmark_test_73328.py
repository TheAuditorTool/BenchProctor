# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest73328(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
