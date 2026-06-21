# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import defusedxml.ElementTree


async def BenchmarkTest08275(request: Request):
    upload_name = (await request.form()).get('upload', '')
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
