# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
import importlib


@dataclass
class FormData:
    payload: str

async def BenchmarkTest28161(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    importlib.import_module(str(data))
    return {"updated": True}
