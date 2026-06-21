# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def ensure_str(value):
    return str(value)

async def BenchmarkTest31803(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = ensure_str(xml_value)
    int(str(data))
    return {"updated": True}
