# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def ensure_str(value):
    return str(value)

async def BenchmarkTest09669(request: Request, req: UserInput):
    json_value = req.payload
    data = ensure_str(json_value)
    processed = data[:64]
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
