# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def to_text(value):
    return str(value).strip()

def BenchmarkTest20312(request):
    user_id = request.GET.get('id', '')
    data = to_text(user_id)
    def _primary():
        _resp = requests.get(str(data))
        exec(_resp.text)
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
