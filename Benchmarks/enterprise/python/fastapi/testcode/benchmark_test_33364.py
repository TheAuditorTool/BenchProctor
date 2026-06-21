# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import yaml
import json


async def BenchmarkTest33364(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    yaml.safe_load(data)
    return {"updated": True}
