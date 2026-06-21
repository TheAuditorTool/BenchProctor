# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import defusedxml.ElementTree


async def BenchmarkTest57647(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
