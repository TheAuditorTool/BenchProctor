# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import importlib


async def BenchmarkTest67275(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    importlib.import_module(str(data))
    return {"updated": True}
