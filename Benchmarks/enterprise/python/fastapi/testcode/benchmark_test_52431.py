# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

async def BenchmarkTest52431(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    importlib.import_module(str(data))
    return {"updated": True}
