# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest01278(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = f'{xml_value:.200s}'
    importlib.import_module(str(data))
    return {"updated": True}
