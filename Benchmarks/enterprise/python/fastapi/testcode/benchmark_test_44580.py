# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest44580(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
