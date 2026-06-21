# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
import importlib
import sys


@dataclass
class FormData:
    payload: str

async def BenchmarkTest45443(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
