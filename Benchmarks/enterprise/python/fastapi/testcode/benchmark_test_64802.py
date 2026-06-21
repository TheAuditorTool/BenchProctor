# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def to_text(value):
    return str(value).strip()

async def BenchmarkTest64802(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = to_text(xml_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
