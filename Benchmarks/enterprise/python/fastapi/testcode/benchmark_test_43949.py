# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest43949(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
