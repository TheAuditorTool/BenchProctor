# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest76661(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
