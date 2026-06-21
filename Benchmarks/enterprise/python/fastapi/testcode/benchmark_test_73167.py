# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


async def BenchmarkTest73167(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(env_value).encode(), _parser)
    return {"updated": True}
