# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import importlib
import sys


@dataclass
class FormData:
    payload: str

async def BenchmarkTest29390(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
