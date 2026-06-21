# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import os
import tempfile


async def BenchmarkTest68451(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
