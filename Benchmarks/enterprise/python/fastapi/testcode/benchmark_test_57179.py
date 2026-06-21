# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest57179(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
