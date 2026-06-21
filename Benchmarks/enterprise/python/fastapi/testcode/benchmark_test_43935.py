# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43935(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
