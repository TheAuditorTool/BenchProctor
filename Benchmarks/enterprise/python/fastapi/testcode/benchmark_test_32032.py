# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from urllib.parse import unquote
from fastapi import Form
import os


async def BenchmarkTest32032(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
