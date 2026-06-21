# SPDX-License-Identifier: Apache-2.0
from fastapi import Request


async def BenchmarkTest55195(request: Request):
    user_id = request.query_params.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return {"updated": True}
