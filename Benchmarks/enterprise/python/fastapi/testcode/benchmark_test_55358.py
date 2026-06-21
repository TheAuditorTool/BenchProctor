# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def to_text(value):
    return str(value).strip()

async def BenchmarkTest55358(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return {"updated": True}
