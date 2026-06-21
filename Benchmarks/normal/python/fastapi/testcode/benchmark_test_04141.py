# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
import os
import tempfile


async def BenchmarkTest04141(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return {"updated": True}
