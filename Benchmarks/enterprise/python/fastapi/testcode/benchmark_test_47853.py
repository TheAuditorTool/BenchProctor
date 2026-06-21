# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


def ensure_str(value):
    return str(value)

async def BenchmarkTest47853(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = ensure_str(header_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
