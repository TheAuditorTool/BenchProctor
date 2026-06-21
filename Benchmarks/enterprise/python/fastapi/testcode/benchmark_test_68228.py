# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest68228(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
