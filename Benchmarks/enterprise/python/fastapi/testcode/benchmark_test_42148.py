# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest42148(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value:.200s}'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(data) + '"]')
    return {"updated": True}
