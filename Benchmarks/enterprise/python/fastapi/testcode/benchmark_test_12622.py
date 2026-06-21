# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest12622(request: Request):
    upload_name = (await request.form()).get('upload', '')
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
