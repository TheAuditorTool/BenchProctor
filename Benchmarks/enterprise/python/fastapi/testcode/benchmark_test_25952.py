# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest25952(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content
