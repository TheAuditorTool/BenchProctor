# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest59104(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    def normalize(value):
        return value.strip()
    data = normalize(multipart_value)
    json.loads(data)
    return {"updated": True}
