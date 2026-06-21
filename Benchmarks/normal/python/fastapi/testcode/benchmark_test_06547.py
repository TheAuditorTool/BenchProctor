# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest06547(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = '{}'.format(upload_name)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
