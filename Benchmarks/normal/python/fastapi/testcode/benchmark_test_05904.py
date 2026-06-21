# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import defusedxml.ElementTree


async def BenchmarkTest05904(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
