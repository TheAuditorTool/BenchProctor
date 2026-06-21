# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest75817(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = coalesce_blank(raw_body)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
