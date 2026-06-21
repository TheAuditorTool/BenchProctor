# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import defusedxml.ElementTree


def relay_value(value):
    return value

async def BenchmarkTest13180(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = relay_value(xml_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
