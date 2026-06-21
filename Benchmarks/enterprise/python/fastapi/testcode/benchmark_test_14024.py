# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import importlib
import sys


def to_text(value):
    return str(value).strip()

async def BenchmarkTest14024(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = to_text(xml_value)
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return {"updated": True}
