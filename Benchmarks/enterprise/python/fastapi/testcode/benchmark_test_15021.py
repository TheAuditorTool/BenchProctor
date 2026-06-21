# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest15021(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '%s' % str(multipart_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
