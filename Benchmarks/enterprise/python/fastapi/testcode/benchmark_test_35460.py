# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest35460(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    request.session['data'] = str(data)
    return {"updated": True}
