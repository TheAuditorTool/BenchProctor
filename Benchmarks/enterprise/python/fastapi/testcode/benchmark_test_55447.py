# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from urllib.parse import unquote


async def BenchmarkTest55447(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
