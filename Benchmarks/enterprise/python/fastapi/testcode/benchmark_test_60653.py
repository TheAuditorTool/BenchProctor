# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest60653(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
