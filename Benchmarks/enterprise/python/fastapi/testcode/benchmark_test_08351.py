# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib


async def BenchmarkTest08351(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    importlib.import_module(str(data))
    return {"updated": True}
