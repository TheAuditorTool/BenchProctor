# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from dataclasses import dataclass
from fastapi import Form
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11482(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
