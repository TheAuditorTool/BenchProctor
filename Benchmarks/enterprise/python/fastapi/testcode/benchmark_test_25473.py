# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from lxml import etree
from dataclasses import dataclass
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest25473(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[name="' + str(processed) + '"]')
    return {"updated": True}
