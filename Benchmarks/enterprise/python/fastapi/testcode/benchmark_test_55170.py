# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import os
import tempfile


async def BenchmarkTest55170(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
