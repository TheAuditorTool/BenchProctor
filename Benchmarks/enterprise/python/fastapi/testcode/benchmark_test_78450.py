# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib
import sys


async def BenchmarkTest78450(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
