# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest47773(request: Request):
    origin_value = request.headers.get('origin', '')
    data = coalesce_blank(origin_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
