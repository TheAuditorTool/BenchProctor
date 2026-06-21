# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22935(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(multipart_value))
    return {"updated": True}
