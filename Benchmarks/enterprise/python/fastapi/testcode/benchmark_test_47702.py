# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


async def BenchmarkTest47702(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
