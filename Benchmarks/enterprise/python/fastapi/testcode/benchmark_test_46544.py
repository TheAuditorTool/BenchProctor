# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest46544(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
