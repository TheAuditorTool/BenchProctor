# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest55034(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    yaml.safe_load(data)
    return {"updated": True}
