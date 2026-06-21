# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest54534(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
