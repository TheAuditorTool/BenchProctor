# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os
from types import SimpleNamespace


async def BenchmarkTest41441(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
