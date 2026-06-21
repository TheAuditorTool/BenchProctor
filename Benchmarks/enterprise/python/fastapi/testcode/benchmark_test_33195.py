# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


async def BenchmarkTest33195(request: Request):
    upload_name = request.query_params.get('filename', '')
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
