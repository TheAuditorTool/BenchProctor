# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00025(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
