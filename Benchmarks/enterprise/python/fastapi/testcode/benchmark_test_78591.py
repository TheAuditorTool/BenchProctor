# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import shlex
import json


async def BenchmarkTest78591(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return {"updated": True}
