# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest77184(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % (auth_header,)
    importlib.import_module(str(data))
    return {"updated": True}
