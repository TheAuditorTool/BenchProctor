# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest08006(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
