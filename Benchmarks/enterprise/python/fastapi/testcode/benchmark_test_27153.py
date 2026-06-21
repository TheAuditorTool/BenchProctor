# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest27153(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data, _sep, _rest = str(upload_name).partition('\x00')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
