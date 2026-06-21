# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def normalise_input(value):
    return value.strip()

async def BenchmarkTest80718(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = normalise_input(header_value)
    os.remove(str(data))
    return {"updated": True}
