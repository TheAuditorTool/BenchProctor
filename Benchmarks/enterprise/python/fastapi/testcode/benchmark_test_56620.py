# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from urllib.parse import unquote


async def BenchmarkTest56620(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
