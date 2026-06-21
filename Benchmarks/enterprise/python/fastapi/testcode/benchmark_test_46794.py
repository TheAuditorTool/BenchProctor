# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest46794(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
