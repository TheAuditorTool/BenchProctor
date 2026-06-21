# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03276(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return {"updated": True}
