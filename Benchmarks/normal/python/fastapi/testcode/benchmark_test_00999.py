# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib


async def BenchmarkTest00999(request: Request, field: str = Form('')):
    field_value = field
    data = '%s' % (field_value,)
    importlib.import_module(str(data))
    return {"updated": True}
