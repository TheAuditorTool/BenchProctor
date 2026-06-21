# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest03114(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = FormData(payload=auth_header).payload
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
