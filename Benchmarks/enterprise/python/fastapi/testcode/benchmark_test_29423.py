# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest29423(request: Request, field: str = Form('')):
    field_value = field
    reader = make_reader(field_value)
    data = reader()
    requests.get(str(data))
    return {"updated": True}
