# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib


async def BenchmarkTest31087(request: Request, field: str = Form('')):
    field_value = field
    if field_value:
        data = field_value
    else:
        data = ''
    importlib.import_module(str(data))
    return {"updated": True}
