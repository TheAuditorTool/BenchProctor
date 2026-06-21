# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest33282(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if upload_name:
        data = upload_name
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
