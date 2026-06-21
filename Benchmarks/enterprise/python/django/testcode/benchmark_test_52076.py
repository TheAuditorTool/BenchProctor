# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import json


def BenchmarkTest52076(request):
    user_id = request.GET.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
