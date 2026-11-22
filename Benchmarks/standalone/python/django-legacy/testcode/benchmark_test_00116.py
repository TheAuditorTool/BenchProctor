# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json
from app_runtime import db


def BenchmarkTest00116(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    token = '%032x' % random.Random().getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
