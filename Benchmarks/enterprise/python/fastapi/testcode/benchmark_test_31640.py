# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest31640(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    eval(str(data))
    return {"updated": True}
