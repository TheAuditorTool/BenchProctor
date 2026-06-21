# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest21898(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
