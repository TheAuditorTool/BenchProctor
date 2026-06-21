# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest78619(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = '{}'.format(multipart_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
