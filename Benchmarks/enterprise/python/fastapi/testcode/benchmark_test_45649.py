# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest45649(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = FormData(payload=xml_value).payload
    json.loads(data)
    return {"updated": True}
