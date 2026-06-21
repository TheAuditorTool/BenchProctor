# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


async def BenchmarkTest81013(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    os.remove(str(header_value))
    return {"updated": True}
