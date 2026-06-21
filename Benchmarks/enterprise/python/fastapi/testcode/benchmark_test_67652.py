# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest67652(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
