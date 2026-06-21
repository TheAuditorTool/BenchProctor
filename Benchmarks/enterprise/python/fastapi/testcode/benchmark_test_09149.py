# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest09149(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = FormData(payload=upload_name).payload
    json.loads(data)
    return {"updated": True}
