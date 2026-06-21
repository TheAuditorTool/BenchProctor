# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os
import importlib
import sys


async def BenchmarkTest51458(request: Request, field: str = Form('')):
    field_value = field
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return {"updated": True}
