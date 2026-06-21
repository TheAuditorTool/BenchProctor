# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest02563(request: Request):
    referer_value = request.headers.get('referer', '')
    data = f'{referer_value:.200s}'
    importlib.import_module(str(data))
    return {"updated": True}
