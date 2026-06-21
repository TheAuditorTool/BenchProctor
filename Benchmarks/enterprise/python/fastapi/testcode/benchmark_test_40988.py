# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest40988(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    importlib.import_module(str(data))
    return {"updated": True}
