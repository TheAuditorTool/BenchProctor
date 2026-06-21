# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os
from types import SimpleNamespace


async def BenchmarkTest74512(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
