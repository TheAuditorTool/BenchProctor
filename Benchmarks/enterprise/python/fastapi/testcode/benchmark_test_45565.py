# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import importlib
import sys


@dataclass
class FormData:
    payload: str

async def BenchmarkTest45565(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return {"updated": True}
