# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import os


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest22007(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = default_blank(forwarded_ip)
    if os.environ.get("APP_ENV", "production") != "test":
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
