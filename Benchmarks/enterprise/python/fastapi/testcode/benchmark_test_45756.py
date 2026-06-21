# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest45756(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    request.session['user'] = str(data)
    return {"updated": True}
