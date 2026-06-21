# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest08991(request: Request):
    upload_name = (await request.form()).get('upload', '')
    prefix = ''
    data = prefix + str(upload_name)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
