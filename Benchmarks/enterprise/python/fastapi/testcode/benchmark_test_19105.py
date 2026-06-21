# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19105(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    result = 100 / int(str(data))
    return {"updated": True}
