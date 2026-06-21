# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import defusedxml.ElementTree


async def BenchmarkTest43637(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
