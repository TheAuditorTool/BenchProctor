# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib
import sys


async def BenchmarkTest27890(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
