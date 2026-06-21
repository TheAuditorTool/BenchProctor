# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import tempfile


@dataclass
class FormData:
    payload: str

async def BenchmarkTest10734(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
