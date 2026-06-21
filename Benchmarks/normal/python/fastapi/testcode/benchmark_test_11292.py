# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib


async def BenchmarkTest11292(request: Request, field: str = Form('')):
    field_value = field
    importlib.import_module(str(field_value))
    return {"updated": True}
