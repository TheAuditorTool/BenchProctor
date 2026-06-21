# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
import subprocess


async def BenchmarkTest73612(request: Request):
    origin_value = request.headers.get('origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    subprocess.run([str(data), '--status'], shell=False)
    return {"updated": True}
