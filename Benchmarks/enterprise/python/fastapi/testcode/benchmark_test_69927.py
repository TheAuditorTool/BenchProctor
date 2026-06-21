# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest69927(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
