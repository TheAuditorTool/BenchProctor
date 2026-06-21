# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import importlib


@dataclass
class FormData:
    payload: str

async def BenchmarkTest53813(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    importlib.import_module(str(data))
    return {"updated": True}
