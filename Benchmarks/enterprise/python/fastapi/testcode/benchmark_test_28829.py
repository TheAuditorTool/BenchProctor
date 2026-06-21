# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest28829(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
