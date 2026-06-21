# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest72114(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    os.remove(str(data))
    return {"updated": True}
