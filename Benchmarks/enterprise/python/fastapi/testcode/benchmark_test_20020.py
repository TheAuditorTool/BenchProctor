# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import defusedxml.ElementTree


async def BenchmarkTest20020(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    defusedxml.ElementTree.fromstring(str(env_value))
    return {"updated": True}
