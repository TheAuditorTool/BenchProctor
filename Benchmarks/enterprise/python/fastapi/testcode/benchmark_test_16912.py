# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest16912(request: Request):
    origin_value = request.headers.get('origin', '')
    importlib.import_module(str(origin_value))
    return {"updated": True}
