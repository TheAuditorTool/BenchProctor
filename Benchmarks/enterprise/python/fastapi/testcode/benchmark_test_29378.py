# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import tempfile


@dataclass
class FormData:
    payload: str

async def BenchmarkTest29378(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
