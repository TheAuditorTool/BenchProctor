# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import json
from app_runtime import db


def BenchmarkTest00155(request):
    field_value = request.POST.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return JsonResponse({'token': str(token)}, status=200)
