# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def normalise_input(value):
    return value.strip()

async def BenchmarkTest29052(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = normalise_input(multipart_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
