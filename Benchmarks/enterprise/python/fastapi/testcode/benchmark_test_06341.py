# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest06341(request: Request):
    referer_value = request.headers.get('referer', '')
    data = FormData(payload=referer_value).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
