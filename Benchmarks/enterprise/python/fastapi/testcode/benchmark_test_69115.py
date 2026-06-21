# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest69115(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    json.loads(data)
    return {"updated": True}
