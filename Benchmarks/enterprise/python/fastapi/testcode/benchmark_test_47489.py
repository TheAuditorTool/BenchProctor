# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from urllib.parse import unquote
from fastapi import Form


async def BenchmarkTest47489(request: Request, field: str = Form('')):
    field_value = field
    data = unquote(field_value)
    os.remove(str(data))
    return {"updated": True}
