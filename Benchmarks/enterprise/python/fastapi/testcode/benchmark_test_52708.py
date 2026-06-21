# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
from urllib.parse import unquote


async def BenchmarkTest52708(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return {"updated": True}
