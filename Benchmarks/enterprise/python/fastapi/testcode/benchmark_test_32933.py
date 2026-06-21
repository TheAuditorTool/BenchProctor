# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree


request_state: dict[str, str] = {}

async def BenchmarkTest32933(request: Request):
    referer_value = request.headers.get('referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    async def _evasion_task():
        tree = etree.fromstring(b'<users><user name="admin"/></users>')
        tree.xpath('/users/user[name="' + str(data) + '"]')
    await _evasion_task()
    return {"updated": True}
