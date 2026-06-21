# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest69316(request: Request):
    upload_name = (await request.form()).get('upload', '')
    prefix = ''
    data = prefix + str(upload_name)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
