# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest63425(request: Request):
    upload_name = (await request.form()).get('upload', '')
    size = min(int(upload_name) if str(upload_name).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
