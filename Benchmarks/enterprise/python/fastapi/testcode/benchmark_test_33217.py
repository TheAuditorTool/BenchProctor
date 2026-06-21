# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest33217(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    request.session['user'] = str(data)
    return {"updated": True}
