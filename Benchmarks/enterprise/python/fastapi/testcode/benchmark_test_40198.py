# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib
import sys


async def BenchmarkTest40198(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
