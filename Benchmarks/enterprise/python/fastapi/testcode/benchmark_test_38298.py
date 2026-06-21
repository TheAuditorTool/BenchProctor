# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest38298(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
