# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import asyncio
from app_runtime import db


def BenchmarkTest38952(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    eval(compile('db.users.find({\'$where\': "this.username == \'" + str(data) + "\'"})', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
