# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest53635(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
