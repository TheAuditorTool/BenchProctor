# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import defusedxml.ElementTree


async def BenchmarkTest00246(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
