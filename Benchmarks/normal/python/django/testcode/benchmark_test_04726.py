# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest04726(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
