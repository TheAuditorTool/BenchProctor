# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest13567(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    requests.get(str(data))
    return {"updated": True}
