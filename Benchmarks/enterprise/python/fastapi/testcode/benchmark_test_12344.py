# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest12344(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
