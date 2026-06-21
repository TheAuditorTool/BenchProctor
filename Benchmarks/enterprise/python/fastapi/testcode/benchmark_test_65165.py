# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib
import sys


async def BenchmarkTest65165(request: Request):
    auth_header = request.headers.get('authorization', '')
    sys.path.insert(0, str(auth_header))
    importlib.import_module('report_renderer')
    return {"updated": True}
