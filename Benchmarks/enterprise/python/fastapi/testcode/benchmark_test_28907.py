# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest28907(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '%s' % str(referer_value)
    importlib.import_module(str(data))
    return {"updated": True}
