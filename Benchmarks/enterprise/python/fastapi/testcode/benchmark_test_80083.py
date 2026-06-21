# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest80083(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = coalesce_blank(upload_name)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return {"updated": True}
