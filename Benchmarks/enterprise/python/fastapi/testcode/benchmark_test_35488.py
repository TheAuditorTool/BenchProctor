# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest35488(request: Request):
    upload_name = (await request.form()).get('upload', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
