# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import requests


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest70084(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
