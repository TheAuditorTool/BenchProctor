# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml


async def BenchmarkTest16665(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
