# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest02017(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
