# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest05433(request: Request):
    upload_name = (await request.form()).get('upload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
