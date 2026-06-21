# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest24112(request: Request, req: UserInput):
    json_value = req.payload
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(json_value) + '"]')
    return {"updated": True}
