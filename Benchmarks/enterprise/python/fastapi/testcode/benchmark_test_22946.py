# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22946(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
