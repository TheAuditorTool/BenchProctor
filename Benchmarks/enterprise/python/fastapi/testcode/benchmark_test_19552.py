# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os
import importlib


def relay_value(value):
    return value

async def BenchmarkTest19552(request: Request, field: str = Form('')):
    field_value = field
    data = relay_value(field_value)
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return {"updated": True}
