# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest07013(request: Request):
    host_value = request.headers.get('host', '')
    prefix = ''
    data = prefix + str(host_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
