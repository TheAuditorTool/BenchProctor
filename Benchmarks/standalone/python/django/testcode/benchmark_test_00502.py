# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest00502(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    parsed = yaml.safe_load(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
