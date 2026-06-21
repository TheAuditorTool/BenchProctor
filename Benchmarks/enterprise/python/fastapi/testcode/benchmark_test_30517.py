# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30517(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = upload_name if upload_name else 'default'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
