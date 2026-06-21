# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from lxml import etree


async def BenchmarkTest71943(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
