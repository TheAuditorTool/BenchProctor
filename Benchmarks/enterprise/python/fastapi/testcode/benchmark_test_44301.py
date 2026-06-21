# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44301(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = (lambda v: v.strip())(upload_name)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
