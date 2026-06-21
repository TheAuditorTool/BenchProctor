# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest69641(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = f'{upload_name}'
    json.loads(data)
    return {"updated": True}
