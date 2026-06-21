# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest10291(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
