# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10464(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    int(str(data))
    return {"updated": True}
