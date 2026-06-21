# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest00841(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = FormData(payload=xml_value).payload
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
