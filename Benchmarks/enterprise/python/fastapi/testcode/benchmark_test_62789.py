# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest62789(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
