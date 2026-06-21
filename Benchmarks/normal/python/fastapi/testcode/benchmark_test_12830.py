# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os
from types import SimpleNamespace


async def BenchmarkTest12830(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
