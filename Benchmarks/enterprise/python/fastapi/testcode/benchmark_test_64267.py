# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest64267(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    json.loads(data)
    return {"updated": True}
