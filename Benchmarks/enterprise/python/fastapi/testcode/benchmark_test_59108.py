# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59108(request: Request):
    upload_name = (await request.form()).get('upload', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(upload_name))
    return {"updated": True}
