# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest28015(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
