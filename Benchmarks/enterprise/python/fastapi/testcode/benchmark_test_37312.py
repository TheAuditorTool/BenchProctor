# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
import json
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest37312(request: Request, req: UserInput):
    json_value = req.payload
    data = json.loads(json_value).get('value', '')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
