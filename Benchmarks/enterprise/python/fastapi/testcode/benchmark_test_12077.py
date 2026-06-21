# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12077(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return {"updated": True}
