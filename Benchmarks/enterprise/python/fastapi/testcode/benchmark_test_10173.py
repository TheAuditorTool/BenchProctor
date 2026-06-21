# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest10173(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
