# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


async def BenchmarkTest21127(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    json.loads(data)
    return {"updated": True}
