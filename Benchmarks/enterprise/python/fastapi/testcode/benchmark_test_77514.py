# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest77514(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
