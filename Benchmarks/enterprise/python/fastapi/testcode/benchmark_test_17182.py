# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest17182(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
