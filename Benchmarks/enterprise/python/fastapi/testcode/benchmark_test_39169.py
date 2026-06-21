# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39169(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
