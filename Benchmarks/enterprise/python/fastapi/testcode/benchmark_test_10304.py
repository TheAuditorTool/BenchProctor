# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest10304(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
