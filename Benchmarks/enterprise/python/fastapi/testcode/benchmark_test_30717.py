# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest30717(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '%s' % str(header_value)
    int(str(data))
    return {"updated": True}
