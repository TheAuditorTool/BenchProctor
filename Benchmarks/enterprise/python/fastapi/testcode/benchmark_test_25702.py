# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import defusedxml.ElementTree


def relay_value(value):
    return value

async def BenchmarkTest25702(request: Request, field: str = Form('')):
    field_value = field
    data = relay_value(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
