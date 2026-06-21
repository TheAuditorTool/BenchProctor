# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest09342(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
