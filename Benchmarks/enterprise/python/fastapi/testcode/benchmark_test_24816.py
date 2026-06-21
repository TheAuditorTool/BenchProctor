# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest24816(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    sys.path.insert(0, str(forwarded_ip))
    importlib.import_module('report_renderer')
    return {"updated": True}
