# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest61964(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
