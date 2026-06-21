# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

async def BenchmarkTest42854(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = FormData(payload=xml_value).payload
    importlib.import_module(str(data))
    return {"updated": True}
