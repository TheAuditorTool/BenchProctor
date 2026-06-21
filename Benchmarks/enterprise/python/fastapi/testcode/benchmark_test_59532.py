# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest59532(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
