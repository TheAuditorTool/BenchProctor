# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from app_runtime import db


def BenchmarkTest00295(request):
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = '%s' % str(api_value)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return JsonResponse({'error': 'invalid integer'}, status=400)
    processed = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return JsonResponse({"saved": True})
