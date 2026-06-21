# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest03939(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    json.loads(data)
    return {"updated": True}
