# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest23625(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return {"updated": True}
