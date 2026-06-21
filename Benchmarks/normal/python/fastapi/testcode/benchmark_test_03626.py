# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest03626(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
