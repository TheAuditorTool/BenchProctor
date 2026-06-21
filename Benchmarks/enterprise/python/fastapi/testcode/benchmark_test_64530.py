# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
import importlib


async def BenchmarkTest64530(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    importlib.import_module(str(data))
    return {"updated": True}
