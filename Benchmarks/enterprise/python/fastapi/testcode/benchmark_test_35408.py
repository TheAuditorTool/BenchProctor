# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35408(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
