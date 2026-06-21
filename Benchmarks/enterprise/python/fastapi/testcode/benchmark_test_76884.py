# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest76884(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    json.loads(data)
    return {"updated": True}
