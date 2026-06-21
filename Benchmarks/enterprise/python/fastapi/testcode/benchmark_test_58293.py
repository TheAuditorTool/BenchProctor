# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import tempfile


async def BenchmarkTest58293(request: Request):
    upload_name = (await request.form()).get('upload', '')
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(upload_name))
    return {"updated": True}
