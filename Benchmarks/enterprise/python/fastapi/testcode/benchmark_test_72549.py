# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

async def BenchmarkTest72549(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    importlib.import_module(str(data))
    return {"updated": True}
