# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest44433(request: Request):
    referer_value = request.headers.get('referer', '')
    data = FormData(payload=referer_value).payload
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content
