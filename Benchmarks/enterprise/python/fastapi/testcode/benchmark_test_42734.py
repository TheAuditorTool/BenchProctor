# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest42734(request: Request):
    upload_name = (await request.form()).get('upload', '')
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    os.remove(str(data))
    return {"updated": True}
