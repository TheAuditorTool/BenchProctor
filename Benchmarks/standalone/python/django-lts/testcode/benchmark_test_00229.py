# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00229(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    parsed = json.JSONDecoder().decode(str(data))
    return JsonResponse({'parsed': str(parsed)}, status=200)
