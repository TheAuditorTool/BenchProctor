# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
import os
import tempfile


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11969(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
