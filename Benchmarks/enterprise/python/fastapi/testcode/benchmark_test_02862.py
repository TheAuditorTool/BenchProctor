# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from fastapi import Form
import defusedxml.ElementTree


async def BenchmarkTest02862(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
