# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest02101(request: Request):
    origin_value = request.headers.get('origin', '')
    data = coalesce_blank(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        os.unlink('/var/app/data/' + str(data))
    return {"updated": True}
