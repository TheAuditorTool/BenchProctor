# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from lxml import etree


async def BenchmarkTest20763(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(graphql_var).encode(), _parser)
    return {"updated": True}
