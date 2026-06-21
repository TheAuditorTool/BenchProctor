# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile
from fastapi import Form
import os


async def BenchmarkTest09370(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
