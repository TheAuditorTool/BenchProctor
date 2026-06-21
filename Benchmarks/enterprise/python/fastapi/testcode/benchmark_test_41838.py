# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest41838(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    int(str(data))
    return {"updated": True}
