# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


request_state: dict[str, str] = {}

async def BenchmarkTest16870(request: Request):
    auth_header = request.headers.get('authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
