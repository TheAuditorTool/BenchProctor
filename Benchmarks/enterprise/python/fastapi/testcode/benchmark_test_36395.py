# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest36395(request: Request):
    ua_value = request.headers.get('user-agent', '')
    reader = make_reader(ua_value)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
