# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest25985(request: Request):
    origin_value = request.headers.get('origin', '')
    data = '{}'.format(origin_value)
    importlib.import_module(str(data))
    return {"updated": True}
