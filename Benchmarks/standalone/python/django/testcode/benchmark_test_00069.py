# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00069(request):
    user_id = request.GET.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), httponly=True, samesite='Strict')
    return resp
