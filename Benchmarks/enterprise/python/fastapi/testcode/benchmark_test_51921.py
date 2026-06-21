# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json


async def BenchmarkTest51921(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    json.loads(data)
    return {"updated": True}
