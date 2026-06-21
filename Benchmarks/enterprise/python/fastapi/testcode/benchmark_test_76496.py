# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest76496(request: Request):
    user_id = request.query_params.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    yaml.safe_load(data)
    return {"updated": True}
