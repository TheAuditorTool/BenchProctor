# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import requests
import ast
import asyncio


def BenchmarkTest21214(request):
    api_value = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials/').text
    try:
        data = str(ast.literal_eval(api_value))
    except (ValueError, SyntaxError):
        data = api_value
    async def _evasion_task():
        return redirect(str(data))
    return asyncio.run(_evasion_task())
