# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest63238(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
