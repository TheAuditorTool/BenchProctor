# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest24471(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    importlib.import_module(str(forwarded_ip))
    return {"updated": True}
