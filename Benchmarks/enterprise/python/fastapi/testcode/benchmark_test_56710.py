# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest56710(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
