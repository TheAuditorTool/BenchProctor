# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest71916(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
