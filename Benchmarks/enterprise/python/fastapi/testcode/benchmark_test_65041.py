# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import defusedxml.ElementTree


async def BenchmarkTest65041(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
