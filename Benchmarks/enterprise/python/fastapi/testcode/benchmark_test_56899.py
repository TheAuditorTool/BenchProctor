# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import importlib
import sys


async def BenchmarkTest56899(request: Request, field: str = Form('')):
    field_value = field
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
