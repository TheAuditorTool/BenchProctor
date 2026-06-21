# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import tempfile


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11481(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
