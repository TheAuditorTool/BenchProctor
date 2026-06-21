# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest39572(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = '%s' % (header_value,)
    eval(str(data))
    return {"updated": True}
