# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os
import importlib


def normalise_input(value):
    return value.strip()

async def BenchmarkTest08532(request: Request, field: str = Form('')):
    field_value = field
    data = normalise_input(field_value)
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return {"updated": True}
