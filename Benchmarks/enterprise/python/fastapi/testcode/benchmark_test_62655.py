# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import defusedxml.ElementTree


async def BenchmarkTest62655(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
