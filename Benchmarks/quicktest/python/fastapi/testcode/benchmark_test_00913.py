# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from fastapi import Form


async def BenchmarkTest00913(request: Request, field: str = Form('')):
    field_value = field
    data, _sep, _rest = str(field_value).partition('\x00')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
