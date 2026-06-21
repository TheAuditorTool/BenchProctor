# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest22514(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
