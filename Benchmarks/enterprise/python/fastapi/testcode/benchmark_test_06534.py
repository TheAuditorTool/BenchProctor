# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


async def BenchmarkTest06534(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(xml_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
