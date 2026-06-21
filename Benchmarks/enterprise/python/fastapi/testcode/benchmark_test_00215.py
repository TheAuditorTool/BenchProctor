# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import json
from lxml import etree


@dataclass
class FormData:
    payload: str

async def BenchmarkTest00215(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
