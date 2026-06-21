# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest70841(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '%s' % (upload_name,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
