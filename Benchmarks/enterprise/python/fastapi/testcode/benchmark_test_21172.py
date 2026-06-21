# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest21172(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
