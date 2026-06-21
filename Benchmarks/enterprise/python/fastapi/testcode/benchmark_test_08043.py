# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib


async def BenchmarkTest08043(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    importlib.import_module(str(data))
    return {"updated": True}
