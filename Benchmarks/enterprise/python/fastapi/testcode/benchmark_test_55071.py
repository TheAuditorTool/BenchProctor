# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from lxml import etree


async def BenchmarkTest55071(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return {"updated": True}
