# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import defusedxml.ElementTree


async def BenchmarkTest41619(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
