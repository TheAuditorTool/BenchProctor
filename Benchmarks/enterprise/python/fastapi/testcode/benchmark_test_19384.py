# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest19384(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
