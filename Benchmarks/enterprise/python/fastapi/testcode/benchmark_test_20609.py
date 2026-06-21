# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from fastapi import Form


async def BenchmarkTest20609(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
